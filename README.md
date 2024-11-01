Student Management System
Objective

Design and implement a CLI-based Student Management System in Python using OOP principles. The system should manage student records, course enrollments, and grade assignments, with the added capability to save and load data to/from a file.
Table of Contents

    Class Design and Implementation
        Class 1: Person
        Class 2: Student (inherits from Person)
        Class 3: Course
    System Functionalities
        Add Student
        Enroll in Course
        Add Grade
        Display Student Details
        Display Course Details
    Error Handling and File Operations
        Error Handling
        Bonus Challenge: Save and Load Data
    Sample Input Output
        Main Menu
        Example Actions and Outputs

Class Design and Implementation
Class 1: Person

Attributes:

    name (str): Name of the person.
    age (int): Age of the person.
    address (str): Address of the person.

Method:

    display_person_info(): Print the details of the person (name, age, and address).

Class 2: Student (inherits from Person)

Additional Attributes:

    student_id (str): Unique identifier for each student.
    grades (dict): Dictionary containing subjects and their respective grades (e.g., {"Math": "A", "Science": "B"}).
    courses (list): List of courses the student is enrolled in.

Methods:

    add_grade(subject, grade): Add or update the grade for a specified subject.
    enroll_course(course): Enroll the student in a specified course.
    display_student_info(): Print all details of the student, including enrolled courses and grades.

Class 3: Course

Attributes:

    course_name (str): Name of the course.
    course_code (str): Unique course code.
    instructor (str): Name of the instructor.
    students (list): List to store students enrolled in this course.

Methods:

    add_student(student): Add a student to the course.
    display_course_info(): Display the course details and the list of enrolled students.

System Functionalities

Develop a menu-driven CLI for users to interact with the system. Below is a description of the main options and functionalities.
Add Student

    Prompt the user for the following details: name, age, address, and student_id.
    Create a new Student object with these details and add it to the system.

Enroll in Course

    Prompt the user for the student_id and course_code.
    Enroll the student with the specified ID in the course with the specified code.

Add Grade

    Prompt the user for student_id, course_code, and grade.
    Assign or update the grade for the student in the specified course. Ensure the student is enrolled in the course before assigning a grade.

Display Student Details

    Prompt the user for the student_id.
    Retrieve and display the student’s details, including enrolled courses and grades.

Display Course Details

    Prompt the user for the course_code.
    Retrieve and display the course’s details, including the list of enrolled students.

Error Handling and File Operations
Error Handling

    Verify that student_id and course_code exist before processing any operations.
    Ensure grades are only assigned to students for courses in which they are enrolled.

Bonus Challenge: Save and Load Data

Implement two functions to manage file operations:

    save_data(): Save all student and course data to a file in JSON format.
    load_data(): Load data from the file, restoring student, course, and enrollment information when the program restarts.
Sample Input Output
Main Menu

When the program starts, display the main menu:

markdown

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

Example Actions and Outputs

    Add New Student
        Input:

        mathematica

Select Option: 1
Enter Name: Sami
Enter Age: 22
Enter Address: Dhaka
Enter Student ID: S001

Output:

java

    Student Sami (ID: S001) added successfully.

Add New Course

    Input:

    mathematica

Select Option: 2
Enter Course Name: Physics
Enter Course Code: PHY101
Enter Instructor Name: Dr. ABC

Output:

csharp

    Course Physics (Code: PHY101) created with instructor Dr. ABC.

Enroll Student in Course

    Input:

    mathematica

Select Option: 3
Enter Student ID: S001
Enter Course Code: PHY101

Output:

java

    Student Sami (ID: S001) enrolled in Physics (Code: PHY101).

Add Grade for Student

    Input:

    mathematica

Select Option: 4
Enter Student ID: S001
Enter Course Code: PHY101
Enter Grade: A

Output:

css

    Grade A added for Sami in Physics.

Display Student Details

    Input:

    mathematica

Select Option: 5
Enter Student ID: S001

Output:

yaml

    Student Information:
    Name: Sami
    ID: S001
    Age: 22
    Address: Dhaka
    Enrolled Courses: Physics
    Grades: {'Physics': 'A'}

Display Course Details

    Input:

    mathematica

Select Option: 6
Enter Course Code: PHY101

Output:

yaml

    Course Information:
    Course Name: Physics
    Code: PHY101
    Instructor: Dr. ABC
    Enrolled Students: Sami

Save Data to File

    Input:

    vbnet

Select Option: 7

Output:

css

    All student and course data saved successfully.

Load Data from File

    Input:

    vbnet

Select Option: 8

Output:

lua

    Data loaded successfully.

Exit

    Input:

    vbnet

Select Option: 0

Output:

        Exiting Student Management System. Goodbye!

Author

    Mahmudul Hasan

License

This project is licensed under the MIT License.
Acknowledgments

Special thanks to the Python community and all the resources that helped in the creation of this project.
