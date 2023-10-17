from databases import Database
from sqlalchemy import MetaData, Table, Column, Integer, String, create_engine

DATABASE_URL = "sqlite:///./pizza_orders.db"
database = Database(DATABASE_URL)

# Create an SQLAlchemy engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a MetaData object
metadata = MetaData()

# Define the table and its columns
orders_table = Table(
    "orders",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("pizza_type", String, index=True),
    Column("size", String, index=True),
    Column("amount", Integer),
)

# Create the table
metadata.create_all(bind=engine)