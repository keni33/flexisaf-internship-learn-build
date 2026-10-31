from database import engine, Base

# Import models so SQLAlchemy knows about the tables
from models import (
    Patient,
    Doctor,
    Department,
    Appointment
)

def create_tables():
    Base.metadata.create_all(bind=engine)
    print("Hospital database tables created successfully!")


if __name__ == "__main__":
    create_tables()
