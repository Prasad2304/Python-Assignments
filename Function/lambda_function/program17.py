'''49.	Take a list containing student names and marks, use functions and lambda expressions to:
a)	Calculate average marks. 
b)	Filter students scoring above 75. 
c)	Sort students according to marks.
'''

students = [
    ("Amit", 80),
    ("Priya", 90),
    ("Rahul", 65),
    ("Sneha", 75),
    ("Neha", 85)
]

# a) Calculate average marks
def average_marks(students):
    total = sum(map(lambda s: s[1], students))
    return total / len(students)

# b) Filter students scoring above 75
above_75 = list(filter(lambda s: s[1] > 75, students))

# c) Sort students according to marks
sorted_students = sorted(students, key=lambda s: s[1])

print("Average Marks =", average_marks(students))
print("Students scoring above 75 =", above_75)
print("Students sorted by marks =", sorted_students)