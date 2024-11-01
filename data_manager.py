import json
from student import Student
from course import Course

def save_data(students, courses):
    student_data = {sid: student.to_dict() for sid, student in students.items()}
    course_data = {cc: course.to_dict() for cc, course in courses.items()}
    
    with open('students.json', 'w') as student_file:
        json.dump(student_data, student_file)
        
    with open('courses.json', 'w') as course_file:
        json.dump(course_data, course_file)
        
    print("All student and course data saved successfully.")


def load_data():
    try:
        with open('students.json', 'r') as student_file:
            student_data = json.load(student_file)
        with open('courses.json', 'r') as course_file:
            course_data = json.load(course_file)
        
        students = {sid: Student.from_dict(data) for sid, data in student_data.items()}
        courses = {cc: Course.from_dict(data) for cc, data in course_data.items()}

        # Restore student enrollments
        for course in courses.values():
            course.students = [students[student_id] for student_id in course.students]
      

       # Print loaded students
        print("\nLoaded Students:")
        for student_id, student in students.items():
            print(f"ID: {student_id}, Name: {student.name}, Age: {student.age}, Address: {student.address}, Courses: {student.courses}, Grades: {student.grades}")

        # Print loaded courses
        print("\nLoaded Courses:")
        for course_code, course in courses.items():
            student_names = [student.name for student in course.students]
            print(f"Code: {course_code}, Name: {course.course_name}, Instructor: {course.instructor}, Students: {student_names}")

        print("Data loaded successfully.")
        return students, courses
    except FileNotFoundError:
        print("No data file found.")
        return {}, {}