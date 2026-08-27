# Employee involvement in two projects

project1 = {"Amit", "Rahul", "Prasad", "Sneha"}
project2 = {"Prasad", "Sneha", "Rohit", "Neha"}

both_projects = project1.intersection(project2)
print("Employees working on both projects:", both_projects)

only_project1 = project1.difference(project2)
print("Employees only in Project 1:", only_project1)

only_project2 = project2.difference(project1)
print("Employees only in Project 2:", only_project2)

all_employees = project1.union(project2)
print("Total unique employees:", all_employees)