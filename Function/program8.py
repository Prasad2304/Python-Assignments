#8.	Create a function power(base, exponent) to calculate the value of base raised to exponent.def power(base, exponent):
    
def power(base, exponent):
    return base ** exponent

base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))

result = power(base, exponent)
print("Power =", result)