#6.	Define a function to calculate the area of a circle using its radius.

def area_of_circle(r):
    area = 3.14 * r * r
    return area

r = float(input("Enter radius: "))
print("Area of circle =", area_of_circle(r))