#write a python program to compute the cosine series cos(x)=1-x^2/2!+x^4/4!-x^6/6!+...+(-1)^n*x^(2n)/(2n)!

import math

x = float(input("Enter the value of x (in radians):"))
n = int(input("Enter the number of terms (n):"))

cos_x = 0
for i in range(n):
    term = ((-1) **i) *(x**(2*i)) / math.factorial(2*i)
    cos_x += term

print("The value of cos(", x, ") using", n, "terms is:", cos_x)
