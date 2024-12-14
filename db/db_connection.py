from sqlmodel import create_engine

# Crear la base de datos SQLite
sqlite_url = "sqlite:///gastos.db"
engine = create_engine(sqlite_url, echo=True)