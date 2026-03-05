name = input("Enter your name: ")
try:
    age = int(input("Enter your age: "))
    if age < 0:
        print("Age cannot be negative.")
    else:
        if age < 13:
            category = "child"
        elif age < 17 and age >= 13:
            category = "teenager"
        elif age > 18 and age < 59:
            category = "adult"
        elif age >= 60:
            category = "senior citizen"
        print(f"Hello {name}")
        print(f"You are a {category}")
except ValueError:
    print("Invalid age input")