#4.	Create a function simple_interest(p, r, t) to calculate simple interest

def simple_interest(p, r, t):
    si = (p * r * t) / 100
    return si

p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time period: "))

print("Simple Interest =", simple_interest(p, r, t))