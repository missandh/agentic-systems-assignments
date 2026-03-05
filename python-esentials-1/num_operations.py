a = input("Enter the first number: ")
b = input("Enter the second number: ")
try:
    a = int(a)
    b = int(b)
    result = a + b
    print(f"The sum of {a} and {b} is: {result}")
    division_result = a / b
    print(f"The division of {a} by {b} is: {division_result}")
except ValueError:
    print("Invalid input. Please enter valid integers.")
except ZeroDivisionError:
    print("Cannot divide by zero.")    

