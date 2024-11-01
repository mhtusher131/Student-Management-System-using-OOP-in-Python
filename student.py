"""
This file contains the Student  Class.
It's in inherits from the Person class
"""

from person import Person

class Student(Person):

    def __init__(self,name,age,address,student_id):
        super().__init__(name,age,address)
        self.student_id = student_id
        self.grades = {}
        self.courses = []

    
    def add_grade(self,subject,grade):
        self.grades[subject] = grade
    
    def enroll_course(self,course):
        if course not in self.courses:
            self.courses.append(course)

    def display_student_info(self):
        self.display_person_into()
        print(f"Student ID:{self.student_id}")
        print(f"Enrolled Courses:{','.join(self.courses)}")
        print(f"Grades:{self.grades}")

    def to_dict(self):
        return {
            'name': self.name,
            'age': self.age,
            'address': self.address,
            'student_id': self.student_id,
            'courses': self.courses,
            'grades': self.grades
        }
    
    @classmethod
    def from_dict(cls, data):
        student = cls(
            name=data['name'],
            age=data['age'],
            address=data['address'],
            student_id=data['student_id']
        )
        student.courses = data.get('courses', [])
        student.grades = data.get('grades', {})
        return student