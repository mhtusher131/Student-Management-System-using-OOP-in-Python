"""
This file contains the Course  Class
"""
class Course ():

    def __init__(self,course_name,course_code,instructor):
        self.course_name = course_name
        self.course_code = course_code
        self.instructor = instructor
        self.students = []

    def add_student(self,student):
        if student not in self.students:
            self.students.append(student)

    def display_course_info(self):
        print(f"Course Name :{self.course_name}, Code :{self.course_code}, Instructor:{self.instructor}")
        print(f"Enrolled Students: {', '.join([student.name for  student in self.students])}")
       
    def to_dict(self):
        return {
            'course_name': self.course_name,
            'course_code': self.course_code,
            'instructor': self.instructor,
            'students': [student.student_id for student in self.students]
        }
    @classmethod
    def from_dict(cls, data):
        course = cls(
            course_name=data['course_name'],
            course_code=data['course_code'],
            instructor=data['instructor']
        )
        return course



# course1 = Course("Bangla",231,"Taher sir")
# course1.add_student("piash")
# course1.add_student("Noushin")
# course1.add_student("Hasan")
# course1.display_course_info()
# print(course1.students)