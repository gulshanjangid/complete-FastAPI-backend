from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Database
DATABASE_URL = "sqlite:///./school.db"

# Engine
engine = create_engine(DATABASE_URL)

# Base
Base = declarative_base()

# Model
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


# Create table
Base.metadata.create_all(bind=engine)

# Session
SessionLocal = sessionmaker(bind=engine)

db = SessionLocal()

# CREATE
student = Student(
    name="Rahul",
    age=20
)

db.add(student)
db.commit()


# READ
students = db.query(Student).all()

for student in students:
    print(student.id, student.name, student.age)


# CLOSE
db.close()
