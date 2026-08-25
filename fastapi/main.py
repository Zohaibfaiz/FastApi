# from fastapi import Depends, FastAPI, HTTPException
# from sqlalchemy.orm import Session

# from database import Base, engine, get_db
# from models import Student
# from schemas import StudentCreate, StudentResponse

# app = FastAPI()

# # Create all tables
# Base.metadata.create_all(bind=engine)


# @app.get("/")
# def home():
#     return {"message": "Student Management API"}


# # CREATE
# @app.post("/students", response_model=StudentResponse)
# def create_student(student: StudentCreate, db: Session = Depends(get_db)):

#     existing = db.query(Student).filter(Student.email == student.email).first()

#     if existing:
#         raise HTTPException(status_code=400, detail="Email already exists")

#     new_student = Student(
#         name=student.name,
#         email=student.email,
#         age=student.age
#     )

#     db.add(new_student)
#     db.commit()
#     db.refresh(new_student)

#     return new_student


# # READ ALL
# @app.get("/students", response_model=list[StudentResponse])
# def get_students(db: Session = Depends(get_db)):
#     return db.query(Student).all()


# # READ ONE
# @app.get("/students/{student_id}", response_model=StudentResponse)
# def get_student(student_id: int, db: Session = Depends(get_db)):

#     student = db.query(Student).filter(Student.id == student_id).first()

#     if not student:
#         raise HTTPException(status_code=404, detail="Student Not Found")

#     return student


# # UPDATE
# @app.put("/students/{student_id}", response_model=StudentResponse)
# def update_student(student_id: int, updated: StudentCreate, db: Session = Depends(get_db)):

#     student = db.query(Student).filter(Student.id == student_id).first()

#     if not student:
#         raise HTTPException(status_code=404, detail="Student Not Found")

#     student.name = updated.name
#     student.email = updated.email
#     student.age = updated.age

#     db.commit()
#     db.refresh(student)

#     return student


# # DELETE
# @app.delete("/students/{student_id}")
# def delete_student(student_id: int, db: Session = Depends(get_db)):

#     student = db.query(Student).filter(Student.id == student_id).first()

#     if not student:
#         raise HTTPException(status_code=404, detail="Student Not Found")

#     db.delete(student)
#     db.commit()

#     return {"message": "Student Deleted Successfully"}



from fastapi import FastAPI

app = FastAPI()


@app.get("/items/")
async def read_items(q: str | None = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results