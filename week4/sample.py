from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import select

# Create an in-memory SQLite engine with echo=True to see SQL logs
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ ="users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    email: Mapped[str]

print("creating tables-----")
Base.metadata.create_all(engine)
 #best practice context manager  
with Session(engine) as session:
    #Do work here
    #Adding new records to database
    user1 = User(name = "Alice", email="alice@example.com")
    session.add(user1)
    #pending state
    session.commit()
    pass
#session closes automatically
#construct query
stmt = select(User).where(User.name == "Alice")
#execute and fetch
result = session.execute(stmt)
user = result.scalars().first()
#get all
users = session.scalars(select(user)).all()
