from student import Student
from course import Course
from data_manager import save_data,load_data

class StudentManagementSystem:
    def __init__(self):
        self.students = {}
        self.courses ={}

    def add_student(self):
        name = input("Enter Name:")
        age = int(input("Enter Age:"))
        address = input("Enter Address:")
        student_id = input("Enter Stdent ID:")
        if student_id not in self.students:
            self.students[student_id] = Student(name,age,address,student_id)
            print(f"Student {name},(ID:{student_id}) add Successfully.")
        else:
            print("Student Id already Exists.")
    
    def add_course(self):
        course_name = input("Enter Course Name:")
        course_code = input("Enter Course Code:")
        instructor = input("Enter Instructor Name:")
        if course_code not in self.courses:
            self.courses[course_code] = Course(course_name,course_code,instructor)
            print(f"Course{course_name}(Code:{course_code}) created with instructor {instructor}")
        else:
            print("Course code alrady exists.")


    def enroll_in_course(self):
        student_id = input("Enter Student ID: ")
        course_code = input("Enter Course Code: ")
        if student_id in self.students and course_code in self.courses:
            student = self.students[student_id]
            course = self.courses[course_code]
            student.enroll_course(course.course_name)
            course.add_student(student)
            print(f"Student {student.name} (ID: {student_id}) enrolled in {course.course_name} (Code: {course_code}).")
        else:
            print("Invalid Student ID or Course Code.")

    def add_grade(self):
        student_id = input("Enter Student ID: ")
        course_code = input("Enter Course Code: ")
        grade = input("Enter Grade: ")
        if student_id in self.students and course_code in self.courses:
            student = self.students[student_id]
            course_name = self.courses[course_code].course_name
            if course_name in student.courses:
                student.add_grade(course_name, grade)
                print(f"Grade {grade} added for {student.name} in {course_name}.")
            else:
                print(f"Student {student.name} is not enrolled in {course_name}.")
        else:
            print("Invalid Student ID or Course Code.")

    def display_student_details(self):
        student_id = input("Enter Student ID: ")
        if student_id in self.students:
            student = self.students[student_id]
            student.display_student_info()
        else:
            print("Student ID not found.")

    def display_course_details(self):
        course_code = input("Enter Course Code: ")
        if course_code in self.courses:
            course = self.courses[course_code]
            course.display_course_info()
        else:
            print("Course Code not found.")

    def save_data(self):
        save_data(self.students, self.courses)

    def load_data(self):
        self.students, self.courses = load_data()


    def run(self):
        while True:
            print("""
==== Student Management System ====
1. Add New Student
2. Add New Course
3. Enroll Student in Course
4. Add Grade for Student
5. Display Student Details
6. Display Course Details
7. Save Data to File
8. Load Data from File
0. Exit
            """)
            option = input("Select Option: ")
            if option == '1':
                self.add_student()
            elif option == '2':
                self.add_course()
            elif option == '3':
                self.enroll_in_course()
            elif option == '4':
                self.add_grade()
            elif option == '5':
                self.display_student_details()
            elif option == '6':
                self.display_course_details()
            elif option == '7':
                self.save_data()
            elif option == '8':
                self.load_data()
            elif option == '0':
                print("Exiting Student Management System. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")
