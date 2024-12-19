from sqlalchemy import create_engine, inspect
from sqlmodel import SQLModel  # Use SQLModel as the base class for your models
from db.db_connection import engine


def validate_and_create_tables():
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    
    if not tables:
        SQLModel.metadata.create_all(engine)  # Use SQLModel.metadata.create_all
        print("Tables created successfully.")
    else:
        print("Tables already exist.")