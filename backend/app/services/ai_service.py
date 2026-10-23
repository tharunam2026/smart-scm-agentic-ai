import json
import httpx
from app.config import settings

def demo_answer(message, analysis):
    m = message.lower()
    if "supplier" in m:
        return "Supplier analysis:\n" + "\n".join(
            f"{sku}: {v[0]['supplier']} — reliability {v[0]['reliability']*100:.0f}%, lead time {v[0]['lead_time_days']} days."
            for sku,v in analysis["suppliers"].items() if v
        )
    if "inventory" in m or "stock" in m:
        items = [x for x in analysis["inventory_status"] if x["status"] != "Healthy"]
        return "Inventory alerts:\n" + "\n".join(
            f"{x['sku']} ({x['product_name']}): {x['stock']} units, {x['days_of_stock']} days — {x['status']}."
            for x in items
        ) if items else "Inventory is healthy. No immediate stock-out action is required."
    return "Recommended actions:\n" + "\n".join(
        f"{a['priority']}: {a['action']} for {a['sku']} from {a['supplier']} (confidence {a['confidence']}%)."
        for a in analysis["decisions"]
    )

async def chat_with_model(message, analysis):
    if settings.ai_provider.lower() != "openai" or not settings.openai_api_key or not settings.openai_model:
        return demo_answer(message, analysis)
    payload = {
        "model": settings.openai_model,
        "messages": [
            {"role":"system","content":"You are an SCM Decision Assistant. Use only supplied data. Do not invent numbers. Explain recommendations and state that purchase actions need human approval."},
            {"role":"user","content":message+"\nDATA:\n"+json.dumps({
                "inventory":analysis["inventory_status"],"suppliers":analysis["suppliers"],
                "risks":analysis["risks"],"decisions":analysis["decisions"]
            })}
        ],
        "temperature":0.2
    }
    async with httpx.AsyncClient(timeout=30) as client:
        r = await client.post("https://api.openai.com/v1/chat/completions",
                              json=payload, headers={"Authorization":f"Bearer {settings.openai_api_key}"})
        r.raise_for_status()
        return r.json()["choices"][0]["message"]["content"]
