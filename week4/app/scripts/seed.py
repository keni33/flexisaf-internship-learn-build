 # Initial sample data

from datetime import datetime, timedelta

from app.database import SessionLocal, Base, engine
from app.models import Department, Doctor, Patient, Appointment

# Ensure tables exist
Base.metadata.create_all(bind=engine)


def seed_database():
    with SessionLocal() as session:
        try:
            # Avoid inserting duplicate sample records
            if session.query(Patient).filter_by(
                email="alex@example.com"
            ).first():
                print("Sample data already exists.")
                return

            # Departments
            cardiology = Department(
                name="Cardiology",
                description="Heart and cardiovascular care"
            )

            pediatrics = Department(
                name="Pediatrics",
                description="Healthcare for children"
            )

            session.add_all([cardiology, pediatrics])
            session.flush()

            # Doctors
            doctor1 = Doctor(
                name="Dr. James",
                email="james@hospital.test",
                specialization="Cardiology",
                department=cardiology
            )

            doctor2 = Doctor(
                name="Dr. Sarah",
                email="sarah@hospital.test",
                specialization="Pediatrics",
                department=pediatrics
            )

            # Patients
            patient1 = Patient(
                name="Alex Brown",
                email="alex@example.com",
                phone="08000000001"
            )

            patient2 = Patient(
                name="Mary Johnson",
                email="mary@example.com",
                phone="08000000002"
            )

            session.add_all([
                doctor1, doctor2, patient1, patient2
            ])

            session.flush()

            # Appointments
            appointment1 = Appointment(
                patient=patient1,
                doctor=doctor1,
                appointment_date=datetime.now() + timedelta(days=2),
                status="scheduled",
                reason="General consultation"
            )

            appointment2 = Appointment(
                patient=patient2,
                doctor=doctor2,
                appointment_date=datetime.now() + timedelta(days=3),
                status="scheduled",
                reason="Routine check-up"
            )

            session.add_all([appointment1, appointment2])

            session.commit()
            print("Hospital sample data inserted successfully!")

        except Exception:
            session.rollback()
            raise


if __name__ == "__main__":
    seed_database()
