import os
import pytest
from sqlalchemy.exc import IntegrityError
import sys

import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from datetime import datetime, timedelta

from app.models import (
    Department,
    Doctor,
    Patient,
    Appointment
)


def test_department_has_doctors(db_session):
    department = Department(
        name="Cardiology",
        description="Heart care"
    )

    doctor = Doctor(
        name="Dr. James",
        email="james@hospital.test",
        specialization="Cardiology",
        department=department
    )

    db_session.add(doctor)
    db_session.commit()

    # Test department -> doctors
    assert len(department.doctors) == 1
    assert department.doctors[0].name == "Dr. James"

    # Test doctor -> department
    assert doctor.department.name == "Cardiology"


def test_patient_has_appointments(db_session):
    patient = Patient(
        name="Alex Brown",
        email="alex@example.com"
    )

    department = Department(name="General Medicine")

    doctor = Doctor(
        name="Dr. Sarah",
        email="sarah@hospital.test",
        specialization="General Medicine",
        department=department
    )

    appointment = Appointment(
        patient=patient,
        doctor=doctor,
        appointment_date=datetime.now() + timedelta(days=2),
        status="scheduled",
        reason="General consultation"
    )

    db_session.add(appointment)
    db_session.commit()

    # Test patient -> appointments
    assert len(patient.appointments) == 1

    # Test appointment -> patient
    assert appointment.patient.name == "Alex Brown"


def test_doctor_has_appointments(db_session):
    department = Department(name="Pediatrics")

    doctor = Doctor(
        name="Dr. Peter",
        email="peter@hospital.test",
        specialization="Pediatrics",
        department=department
    )

    patient = Patient(
        name="Mary Johnson",
        email="mary@example.com"
    )

    appointment = Appointment(
        patient=patient,
        doctor=doctor,
        appointment_date=datetime.now() + timedelta(days=3),
        status="scheduled"
    )

    db_session.add(appointment)
    db_session.commit()

    # Test doctor -> appointments
    assert len(doctor.appointments) == 1

    # Test appointment -> doctor
    assert appointment.doctor.name == "Dr. Peter"


def test_invalid_appointment_status_is_rejected(db_session):
    department = Department(name="Neurology")

    doctor = Doctor(
        name="Dr. Adams",
        email="adams@hospital.test",
        specialization="Neurology",
        department=department
    )

    patient = Patient(
        name="John Smith",
        email="john@example.com"
    )

    appointment = Appointment(
        patient=patient,
        doctor=doctor,
        appointment_date=datetime.now() + timedelta(days=2),
        status="waiting"
    )

    db_session.add(appointment)

    try:
        db_session.commit()
        pytest.fail("Expected IntegrityError for invalid appointment status")
    except IntegrityError:
        db_session.rollback()
