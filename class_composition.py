from student import Student
'''
Program: class_composition.py
Author: Joshua M. McGinley
Last date modified: 11/08/2022

In this assignment, you will create a class with a data member of the type of a class you defined.
Student is a Person with a major, a start date and a gpa. Use the Person class defined above.
Define a Student class with methods change_major(), update_gpa() and display() that returns a string.
Include a driver that

    Creates a student object (select a meaningful name) with your name, major, start date and 4.0 gpa
    Displays the student
    Changes the major to 'Being Awesome!'
    Updates the gpa to 3.0
    Displays the student
    Performs garbage collection
'''

class Person:
    """Person class using class Address, Class Composition"""
    def __init__(self, lname, fname, stu=''):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.student = stu

    def display(self):
        return 'Name: ' + str(self.first_name) + " " + str(self.last_name) + '\n' + str(self.student.display())

#Driver
if __name__ == '__main__':
    s = Student('Cybersecurity', 'Fall 2022', 4.0)
    p = Person('McGinley', 'Joshua', s)
    print(p.display())
    s.change_major('Being Awesome!')
    s.update_gpa(3.0)
    print(p.display())

