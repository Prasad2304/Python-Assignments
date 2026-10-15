""" 19. Store student attendance records in a file. Calculate the attendance percentage and display 
students having attendance below 75%.  """

import csv

def calculate_attendance(students):
    print("Student Attendance Records:")

    for s in students:
        total = int(s["TotalClasses"])
        present = int(s["Present"])

        percentage = (present / total) * 100

        print(s["RollNo"], s["Name"], percentage, "%")

        if percentage < 75:
            print("Attendance Below 75%:", s["Name"])


with open(r"C:\Users\Prasad\Desktop\Python\File_Handling\attendance19.txt", "r") as file:
    reader = csv.DictReader(file)
    students = list(reader)

calculate_attendance(students)