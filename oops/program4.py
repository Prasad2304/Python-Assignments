#hybrid inheritance

class University:
    def university_name(self):
        print("University: Pune University")

class College(University):
    def college_name(self):
        print("College: ABC College")
        self.university_name()

class Student(College):
    def student_name(self):
        print("Student: Prasad")
        self.college_name()
        self.university_name()

student = Student()
student.student_name()
