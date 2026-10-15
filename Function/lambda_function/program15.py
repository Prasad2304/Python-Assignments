#47.Take a list of tuples containing student names and marks, sort the students according to their marks using lambda.

students = [("Alice", 85), ("Bob", 90), ("Charlie", 78), ("David", 95)]

sorted_students = sorted(students, key=lambda student: student[1])

print("Students sorted by marks =", sorted_students)