try:
    num = int(input("Enter number: "))
    result = 10 / num

except ValueError:
    print("Invalid input")

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Result:", result)

finally:
    print("Program execution completed")