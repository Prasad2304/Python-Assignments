#multilevel inheritance

class University:
    def university_name(self):
        print("University: Pune University")


class College(University):
    def college_name(self):
        print("College: ABC College")


class Student(College):
    def student_name(self):
        print("Student: Prasad")


student = Student()

student.university_name()
student.college_name()
student.student_name()