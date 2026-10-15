import csv

def display_employees(employees):
    print("All Employees:")
    for e in employees:
        print(e["EmpID"], e["Name"], e["Department"], e["Salary"])


def highest_paid_employee(employees):
    employee = max(employees, key=lambda e: int(e["Salary"]))
    print("\nHighest Paid Employee:")
    print(employee["Name"], employee["Salary"])


def average_salary(employees):
    total = sum(int(e["Salary"]) for e in employees)
    average = total / len(employees)
    print("\nAverage Salary:", average)


def employees_above_salary(employees, salary):
    print("\nEmployees Earning Above", salary, ":")
    for e in employees:
        if int(e["Salary"]) > salary:
            print(e["Name"], e["Salary"])


with open(r"C:\Users\Prasad\Desktop\Python\File_Handling\employees18.txt", "r") as file:
    reader = csv.DictReader(file)
    employees = list(reader)

display_employees(employees)
highest_paid_employee(employees)
average_salary(employees)

salary = int(input("\nEnter salary limit: "))
employees_above_salary(employees, salary)