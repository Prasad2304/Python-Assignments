#48.Take employee records containing name and salary, sort them according to salary using lambda.

employees = [("Alice", 50000), ("Bob", 60000), ("Charlie", 45000), ("David", 70000)]

sorted_employees = sorted(employees, key=lambda employee: employee[1])

print("Employees sorted by salary =", sorted_employees)