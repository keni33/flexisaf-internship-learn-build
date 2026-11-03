# Connection and sessions
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.exc import IntegrityError

#create database
engine = create_engine("sqlite:///tasks.db", echo=False)
Base = declarative_base()
session = sessionmaker()
session = session()

#Define models(users/tasks)
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
     #this makes it a parent to the table tasks and if i delete a user it refereces it in the child
    task = relationship('Task', back_populates='user', cascade="all, delete-orphan")
#making relationships
class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=True)
    description = Column(String)
    user_id = Column(Integer, ForeignKey('users.id')) #foreign key allows us to speah to other models
    user = relationship('User', back_populates='tasks')


Base.metadata.create_all(engine)

#utility functions
def get_user_by_email(email):
    return session.query(User).filterby(email=email).first()

def confirm_action(prompt:str) -> bool:
    return input(f"{prompt} (yes/no): ").strip().lower() == 'yes'

#CRUD opeeration
def add_user():
    name,email = input("Enter username:"), input("Enter email:")
    if get_user_by_email:
        print('User already exists: {email}')
        return

    try:
        session.add(User(name=name, email=email))
        session.commit()
        print(f'User: {name} added!')
    except IntegrityError:
        session.rolback()
        print(f'ERROR')

def add_task():
    email = input("Enter the email of the user to add tasks: ")
    user = get_user_by_email(email)
    if not user:
        print(f'No user found with this email!')
        return

    title, description = input("Enter the title:"), input("Enter the description")
    session.add(Task(title=title, description=description))
    session.commit()
    print("Addded to database {title}:{description}")

def query_users():
    for user in session.query(User).all():
        

#main ops
def main() ->None:
    actions = {
        "1": add_user,
        "2": add_task
    }
    while True:
        print("\nOptions:\n1. Add User\n 2. Add Task\n3. Query Users\n4. Query Tasks\n5. Update User\n6. Delete User\n7. Delete Tasks\n8. Exit")
        choice = input("Enter an Option: ")
        if choice == "8":
            print("Adios")
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print("That is not an option")


if __name__ == "__main__":
    main()
