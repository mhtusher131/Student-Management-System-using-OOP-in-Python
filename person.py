"""
This file contains the Person Class
"""
class Person:

    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address


    def display_person_into(self):
        print(f"Name :{self.name}")
        print(f"Age:{self.age}")
        print(f"Address:{self.address}")


# p1 = Person("Tusher",21,"Dhaka")
# p1.display_person_into()

