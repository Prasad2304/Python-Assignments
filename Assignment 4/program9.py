# Attendance System using File Handling

attendance = {}

# Read attendance from file
with open(r"C:\Users\Prasad\Desktop\Python\Assignment 4\sample_9.txt", "r") as file:
    for line in file:
        day, students = line.strip().split(":")
        
        # Convert students into a set
        student_set = set(students.split(","))
        
        # Store in dictionary
        attendance[day] = student_set


# Find students who attended all classes
all_students = set.intersection(*attendance.values())


# Count attendance of each student
student_count = {}

for students in attendance.values():
    for student in students:
        if student in student_count:
            student_count[student] += 1
        else:
            student_count[student] = 1


# Find students who attended only one class
only_one_class = set()

for student, count in student_count.items():
    if count == 1:
        only_one_class.add(student)


# Find total unique students
unique_students = set.union(*attendance.values())


# Display results
print("Students who attended all classes:")
print(all_students)

print("\nStudents who attended only one class:")
print(only_one_class)

print("\nTotal unique students:")
print(len(unique_students))