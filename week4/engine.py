
from sqlalchemy import create_engine

# Create an in-memory SQLite engine with echo=True to see SQL logs
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)