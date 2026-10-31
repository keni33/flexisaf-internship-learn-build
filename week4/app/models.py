from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime,
    Text,
    CheckConstraint
)

from sqlalchemy.orm import relationship

from app.database import Base



# 1. DEPARTMENT MODEL

class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=True)

    # One department can have many doctors
    doctors = relationship(
        "Doctor",
        back_populates="department"
    )


# 2. DOCTOR MODEL

class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    specialization = Column(String(100), nullable=False)

    department_id = Column(
        Integer,
        ForeignKey("departments.id"),
        nullable=False
    )

    # Connect doctor to department
    department = relationship(
        "Department",
        back_populates="doctors"
    )

    # One doctor can have many appointments
    appointments = relationship(
        "Appointment",
        back_populates="doctor"
    )


# 3. PATIENT MODEL

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(20), nullable=True)

    # One patient can have many appointments
    appointments = relationship(
        "Appointment",
        back_populates="patient"
    )


# 4. APPOINTMENT MODEL

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True)

    patient_id = Column(
        Integer,
        ForeignKey("patients.id"),
        nullable=False
    )

    doctor_id = Column(
        Integer,
        ForeignKey("doctors.id"),
        nullable=False
    )

    appointment_date = Column(DateTime, nullable=False)

    status = Column(
        String(30),
        nullable=False,
        default="scheduled"
    )

    reason = Column(Text, nullable=True)

    # Only allow recognized appointment statuses
    __table_args__ = (
        CheckConstraint(
            "status IN ('scheduled', 'completed', 'cancelled')",
            name="valid_appointment_status"
        ),
    )

    # Connect appointment to patient
    patient = relationship(
        "Patient",
        back_populates="appointments"
    )

    # Connect appointment to doctor
    doctor = relationship(
        "Doctor",
        back_populates="appointments"
    )
