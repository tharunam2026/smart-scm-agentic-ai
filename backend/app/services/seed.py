from sqlalchemy.orm import Session
from app.models.models import Inventory, Supplier, Order

def seed_database(db: Session):
    if db.query(Inventory).count() > 0:
        return False
    db.add_all([
        Inventory(sku="FAB-001", product_name="Cotton Fabric", stock=420, reorder_level=300, daily_demand=70, unit_cost=145),
        Inventory(sku="FAB-002", product_name="Polyester Fabric", stock=180, reorder_level=250, daily_demand=55, unit_cost=120),
        Inventory(sku="YRN-001", product_name="Cotton Yarn", stock=900, reorder_level=500, daily_demand=80, unit_cost=210),
        Inventory(sku="YRN-002", product_name="Blended Yarn", stock=160, reorder_level=220, daily_demand=45, unit_cost=185),
        Inventory(sku="ACC-001", product_name="Zipper", stock=1200, reorder_level=700, daily_demand=90, unit_cost=18),
    ])
    db.add_all([
        Supplier(name="Tamil Textiles Supply", sku="FAB-001", lead_time_days=4, reliability=.94, unit_price=142),
        Supplier(name="South Looms Pvt Ltd", sku="FAB-001", lead_time_days=6, reliability=.89, unit_price=138),
        Supplier(name="Coimbatore Fibres", sku="FAB-002", lead_time_days=5, reliability=.91, unit_price=116),
        Supplier(name="Erode Yarn Works", sku="YRN-001", lead_time_days=3, reliability=.96, unit_price=205),
        Supplier(name="Salem Spinners", sku="YRN-002", lead_time_days=7, reliability=.86, unit_price=178),
        Supplier(name="Chennai Accessories", sku="ACC-001", lead_time_days=5, reliability=.92, unit_price=17),
    ])
    db.add_all([
        Order(sku="FAB-001", quantity=500, status="In Transit", supplier="Tamil Textiles Supply", expected_date="2026-10-08"),
        Order(sku="YRN-001", quantity=300, status="Confirmed", supplier="Erode Yarn Works", expected_date="2026-10-09"),
        Order(sku="ACC-001", quantity=600, status="Pending", supplier="Chennai Accessories", expected_date="2026-10-11"),
    ])
    db.commit()
    return True
