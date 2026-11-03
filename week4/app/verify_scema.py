
from sqlalchemy import inspect
from database import engine

inspector = inspect(engine)

tables = inspector.get_table_names()

print("Tables in hospital database:")

for table in tables:
    print(f"\n{table.upper()}")

    for column in inspector.get_columns(table):
        print(
            f"  {column['name']} "
            f"({column['type']}) "
            f"Nullable: {column['nullable']}"
        )
