from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import engine, Base, get_db
import app.models.models as models

# Create all Database Tables on Application Startup
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Smart SCM - Agentic AI Integrated System",
    description="Textile Supply Chain Management & Production Rescheduling API",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to Smart SCM Agentic AI API",
        "status": "Running",
        "docs": "http://localhost:8000/docs"
    }

@app.get("/api/health")
def health_check():
    return {"status": "Healthy", "database": "Connected"}

@app.get("/api/dashboard")
def get_dashboard_metrics(db: Session = Depends(get_db)):
    from app.models.models import CustomerOrder, Material, Machine
    
    total_orders = db.query(CustomerOrder).count()
    pending_orders = db.query(CustomerOrder).filter(CustomerOrder.status == "Pending").count()
    completed_orders = db.query(CustomerOrder).filter(CustomerOrder.status == "Completed").count()
    delayed_orders = db.query(CustomerOrder).filter(CustomerOrder.status == "Delayed").count()
    
    total_materials = db.query(Material).count()
    low_stock_materials = db.query(Material).filter(Material.available_stock <= Material.reorder_level).count()
    
    total_machines = db.query(Machine).count()
    active_machines = db.query(Machine).filter(Machine.status == "Available").count()
    
    return {
        "metrics": {
            "total_orders": total_orders,
            "pending_orders": pending_orders,
            "completed_orders": completed_orders,
            "delayed_orders": delayed_orders,
            "total_materials": total_materials,
            "low_stock_materials": low_stock_materials,
            "total_machines": total_machines,
            "active_machines": active_machines
        },
        "status": "success"
    }