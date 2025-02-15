# student/services.py
from .repositories import StudentRepository

class StudentService:
    def __init__(self, repository):
        self.repository = repository
    
    def list_students(self):
        return self.repository.get_all()
    
    def get_student(self, student_id):
        return self.repository.get_by_id(student_id)
    
    def create_student(self, data):
        return self.repository.create(data)
    
    def update_student(self, student_id, data):
        return self.repository.update(student_id, data)
    
    def delete_student(self, student_id):
        return self.repository.delete(student_id)