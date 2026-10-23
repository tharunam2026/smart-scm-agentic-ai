from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.models import Inventory, Supplier, Order
from app.services.seed import seed_database
from app.agents.orchestrator import AgentOrchestrator
from app.schemas import ChatRequest
from app.services.ai_service import chat_with_model

router = APIRouter(prefix="/api")

def seed(db): seed_database(db)

@router.get("/health")
def health(): return {"status":"ok"}

@router.post("/seed")
def seed_route(db: Session=Depends(get_db)):
    return {"seeded": seed_database(db)}

@router.get("/inventory")
def inventory(db: Session=Depends(get_db)):
    seed(db)
    return [{"id":x.id,"sku":x.sku,"product_name":x.product_name,"stock":x.stock,"reorder_level":x.reorder_level,"daily_demand":x.daily_demand,"unit_cost":x.unit_cost} for x in db.query(Inventory).all()]

@router.get("/suppliers")
def suppliers(db: Session=Depends(get_db)):
    seed(db)
    return [{"id":x.id,"name":x.name,"sku":x.sku,"lead_time_days":x.lead_time_days,"reliability":x.reliability,"unit_price":x.unit_price} for x in db.query(Supplier).all()]

@router.get("/orders")
def orders(db: Session=Depends(get_db)):
    seed(db)
    return [{"id":x.id,"sku":x.sku,"quantity":x.quantity,"status":x.status,"supplier":x.supplier,"expected_date":x.expected_date} for x in db.query(Order).all()]

@router.get("/dashboard")
def dashboard(db: Session=Depends(get_db)):
    seed(db)
    inv, sup, orders = db.query(Inventory).all(), db.query(Supplier).all(), db.query(Order).all()
    a = AgentOrchestrator().analyze(inv,sup,orders)
    return {"kpis":{
        "inventory_value":round(sum(x.stock*x.unit_cost for x in inv),2),
        "products":len(inv),
        "critical_items":sum(x["status"]=="Critical" for x in a["inventory_status"]),
        "pending_orders":sum(x.status in ["Pending","Confirmed"] for x in orders)
    },"inventory":a["inventory_status"],"risks":a["risks"],"actions":a["decisions"],"supplier_count":len(sup)}

@router.post("/ai/analyze")
def analyze(db: Session=Depends(get_db)):
    seed(db)
    return AgentOrchestrator().analyze(db.query(Inventory).all(),db.query(Supplier).all(),db.query(Order).all())

@router.post("/ai/chat")
async def chat(req: ChatRequest, db: Session=Depends(get_db)):
    seed(db)
    a=AgentOrchestrator().analyze(db.query(Inventory).all(),db.query(Supplier).all(),db.query(Order).all())
    return {"answer":await chat_with_model(req.message,a),"agent_decisions":a["decisions"]}
