class AgentOrchestrator:
    def analyze(self, inventory, suppliers, orders):
        demand = {}
        inv_status = []
        supplier_map = {}
        procurement = []
        risks = []

        for x in inventory:
            demand[x.sku] = {
                "daily_demand": x.daily_demand,
                "projected_7_day_demand": round(x.daily_demand * 7),
                "trend": "High" if x.daily_demand >= 70 else "Moderate"
            }
            days = round(x.stock / x.daily_demand, 1) if x.daily_demand else 999
            status = "Critical" if x.stock < x.reorder_level else ("Watch" if x.stock <= x.reorder_level * 1.25 else "Healthy")
            inv_status.append({
                "sku": x.sku, "product_name": x.product_name, "stock": x.stock,
                "reorder_level": x.reorder_level, "days_of_stock": days, "status": status
            })

        for s in suppliers:
            score = round(s.reliability*70 + max(0,14-s.lead_time_days)/14*20 + max(0,250-s.unit_price)/250*10, 1)
            supplier_map.setdefault(s.sku, []).append({
                "supplier": s.name, "lead_time_days": s.lead_time_days,
                "reliability": s.reliability, "unit_price": s.unit_price, "score": score
            })
        for sku in supplier_map:
            supplier_map[sku].sort(key=lambda z: z["score"], reverse=True)

        for x in inventory:
            if x.stock < x.reorder_level:
                target = round(x.daily_demand*7 + x.reorder_level*.5)
                qty = max(0, target-x.stock)
                procurement.append({
                    "sku": x.sku, "recommended_quantity": qty,
                    "reason": f"Stock {x.stock} is below reorder level {x.reorder_level}"
                })
                best = supplier_map.get(x.sku, [None])[0]
                risks.append({
                    "sku": x.sku,
                    "risk": "High" if x.stock/max(x.daily_demand,1) < 3 else "Medium",
                    "best_supplier": best["supplier"] if best else "No supplier found",
                    "message": f"{x.product_name} may face stock-out risk."
                })

        actions = []
        for r in procurement:
            best = supplier_map.get(r["sku"], [None])[0]
            actions.append({
                "priority":"HIGH", "sku":r["sku"],
                "action":f"Purchase {r['recommended_quantity']} units",
                "supplier":best["supplier"] if best else "Select supplier",
                "why":r["reason"], "confidence":round((best["reliability"] if best else .7)*100)
            })
        if not actions:
            actions.append({"priority":"LOW","sku":"-","action":"No immediate procurement required",
                            "supplier":"-","why":"Current stock is above reorder levels.","confidence":90})

        return {
            "demand": demand, "inventory_status": inv_status,
            "suppliers": supplier_map, "procurement": procurement,
            "risks": risks, "decisions": actions
        }
