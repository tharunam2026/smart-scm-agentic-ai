from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    product_code = Column(String, unique=True, index=True)
    name = Column(String, nullable=False)
    category = Column(String) # e.g., Cotton Shirt, Denim Yarn
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class Material(Base):
    __tablename__ = "materials"

    id = Column(Integer, primary_key=True, index=True)
    material_code = Column(String, unique=True, index=True)
    name = Column(String, nullable=False)
    category = Column(String) # e.g., Yarn, Fabric, Dye, Chemical
    unit = Column(String, default="kg") # e.g., kg, meters, liters
    available_stock = Column(Float, default=0.0)
    reorder_level = Column(Float, default=100.0)
    unit_cost = Column(Float, default=0.0)

class CustomerOrder(Base):
    __tablename__ = "customer_orders"

    id = Column(Integer, primary_key=True, index=True)
    order_number = Column(String, unique=True, index=True)
    customer_name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    priority = Column(String, default="Medium") # Low, Medium, High
    status = Column(String, default="Pending") # Pending, Scheduled, Completed, Delayed
    order_date = Column(DateTime, default=datetime.utcnow)
    delivery_deadline = Column(DateTime, nullable=False)

class Machine(Base):
    __tablename__ = "machines"

    id = Column(Integer, primary_key=True, index=True)
    machine_code = Column(String, unique=True, index=True)
    name = Column(String, nullable=False)
    capacity_per_hour = Column(Float, default=50.0)
    status = Column(String, default="Available") # Available, Maintenance, Busy