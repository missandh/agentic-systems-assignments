firstname = input("Enter your first name: ")
lastname = input("Enter your last name: ")
try:
    age = int(input("Enter your age: "))
    if age < 0:
        print("Age cannot be negative.")
    print(f"Full Name: {firstname} {lastname}")
    print(f"You will be {age + 1} next year.")
except ValueError:
    print("Invalid age input")


