import csv

with open(r"C:\Users\Prasad\Desktop\Python\File_Handling\csv17.txt","r") as file:
    reader = csv.DictReader(file)
    students = list(reader)

print("All Student Records:")
for s in students:
    print(s["RollNo"], s["Name"], s["Marks"])

topper = max(students, key=lambda s: int(s["Marks"]))
print("\nHighest Marks:")
print(topper["Name"], topper["Marks"])

total = sum(int(s["Marks"]) for s in students)
average = total / len(students)
print("\nAverage Marks:", average)

print("\nStudents Scoring More Than 80:")
for s in students:
    if int(s["Marks"]) > 80:
        print(s["Name"], s["Marks"])