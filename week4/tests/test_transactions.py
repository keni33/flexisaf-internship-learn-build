
import pytest
from sqlalchemy.exc import IntegrityError

from app.models import Department


def test_commit_saves_department(db_session):
    department = Department(name="Cardiology")

    db_session.add(department)
    db_session.commit()

    saved_department = (
        db_session.query(Department)
        .filter_by(name="Cardiology")
        .first()
    )

    assert saved_department is not None
    assert saved_department.name == "Cardiology"


def test_rollback_discards_uncommitted_department(db_session):
    department = Department(name="Neurology")

    db_session.add(department)
    db_session.rollback()

    saved_department = (
        db_session.query(Department)
        .filter_by(name="Neurology")
        .first()
    )

    assert saved_department is None


def test_session_recovers_after_integrity_error(db_session):
    first_department = Department(name="Emergency")
    db_session.add(first_department)
    db_session.commit()

    duplicate_department = Department(name="Emergency")
    db_session.add(duplicate_department)

    with pytest.raises(IntegrityError):
        db_session.commit()

    db_session.rollback()

    another_department = Department(name="Radiology")
    db_session.add(another_department)
    db_session.commit()

    saved_department = (
        db_session.query(Department)
        .filter_by(name="Radiology")
        .first()
    )

    assert saved_department is not None
