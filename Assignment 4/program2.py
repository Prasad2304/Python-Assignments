#2.	Write a program to develope a system that manages the positions of points in a 2D plane.
# The position of each point is represented as a tuple of two values: (x, y). Write a program that:
import math

def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def farthest_from_origin(points):
    farthest_point = points[0]
    max_distance = distance((0, 0), points[0])

    for point in points:
        d = distance((0, 0), point)

        if d > max_distance:
            max_distance = d
            farthest_point = point

    return farthest_point, max_distance

n = int(input("Enter number of points: "))

points = []

for i in range(n):
    x = int(input("Enter x coordinate: "))
    y = int(input("Enter y coordinate: "))

    points.append((x, y))

print("\nPoints:", points)

p1 = tuple(map(int, input("\nEnter first point (x y): ").split()))
p2 = tuple(map(int, input("Enter second point (x y): ").split()))

print("Distance between points:", distance(p1, p2))

point, dist = farthest_from_origin(points)

print("Farthest point from origin:", point)
print("Distance from origin:", dist)