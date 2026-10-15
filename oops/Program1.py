#single inheritance

class Person:
    def show_name(self):
        print("Name: Prasad")


class Student(Person):
    def show_course(self):
        print("Course: Computer Science")


student = Student()

student.show_name()
student.show_course()