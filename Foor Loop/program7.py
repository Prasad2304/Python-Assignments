#write a short python program to check th weather the square root the number is prime or not

import math

n = int(input("Enter a number: "))

root = int(math.sqrt(n))
is_prime = True

if root < 2:
    is_prime = False
else:
    for i in range(2, root):
        if root % i == 0:
            is_prime = False
            break

if is_prime:
    print("Square root is prime")
else:
    print("Square root is not prime")