from sqlmodel import create_engine, SQLModel, Session
from contextlib import contextmanager

# Crear la base de datos SQLite
sqlite_url = "sqlite:///gastos.db"
engine = create_engine(sqlite_url, echo=True)


@contextmanager
def get_session():
    with Session(engine) as session:
        yield session