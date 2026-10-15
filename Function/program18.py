#18.Create a function that accepts marks in five subjects and returns the student's percentage and grade.

def calculate_result(m1, m2, m3, m4, m5):
    total = m1 + m2 + m3 + m4 + m5
    percentage = total / 5

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 35:
        grade = "D"
    else:
        grade = "Fail"

    return percentage, grade

m1 = int(input("Enter marks in subject 1: "))
m2 = int(input("Enter marks in subject 2: "))
m3 = int(input("Enter marks in subject 3: "))
m4 = int(input("Enter marks in subject 4: "))
m5 = int(input("Enter marks in subject 5: "))

percentage, grade = calculate_result(m1, m2, m3, m4, m5)

print("Percentage =", percentage, "%")
print("Grade =", grade)