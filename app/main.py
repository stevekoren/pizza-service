from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pydantic import Field
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.database import database

app = FastAPI()

# Create the SQLAlchemy engine based on the configured database
DATABASE_URL = "sqlite:///./pizza_orders.db"

# SQLAlchemy Setup
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Pydantic model for order data validation
class PizzaOrder(BaseModel):
    pizza_type: str = Field(..., alias="pizza-type")
    size: str
    amount: int


# Pydantic model for order response
class Order(BaseModel):
    id: int
    pizza_type: str = Field(..., alias="pizza-type")
    size: str
    amount: int


class PizzaOrderModel(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    pizza_type = Column(String, index=True)
    size = Column(String, index=True)
    amount = Column(Integer)


Base.metadata.create_all(bind=engine)


# API Routes
@app.get("/health")
async def get_health():
    return {"status": "OK"}


@app.post("/order")
async def create_order(order: PizzaOrder):
    # Create an order in the database
    db = SessionLocal()
    db_order = PizzaOrderModel(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    db.close()

    return {"order_id": db_order.id, **order.dict()}


@app.get("/orders")
async def get_orders(skip: int = 0, limit: int = 10):
    # Fetch a list of orders from the database with optional pagination
    db = SessionLocal()
    orders = db.query(PizzaOrderModel).offset(skip).limit(limit).all()
    db.close()

    return orders


# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "OK"}


# CORS middleware
origins = ["*"]  # You should specify your allowed origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
