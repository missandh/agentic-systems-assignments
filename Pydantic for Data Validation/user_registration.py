from pydantic import BaseModel, Field, ValidationError, EmailStr, ConfigDict

class UserRegister(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    
    username: str = Field(..., min_length=5, description="Username must be at least 5 characters")
    email: EmailStr = Field(..., description="Must be a valid email address")
    age: int = Field(..., ge=18, description="Age must be 18 or older")

# Example usage and validation
if __name__ == "__main__":
    # Valid user data
    try:
        user1 = UserRegister(username="johndoe", email="john@example.com", age=25)
        print("Valid user created:")
        print(f"Username: {user1.username}")
        print(f"Email: {user1.email}")
        print(f"Age: {user1.age}")
    except ValidationError as e:
        print(f"Validation error: {e}")

    print("\n" + "="*50 + "\n")

    # Invalid user data examples
    invalid_users = [
        {"username": "abc", "email": "invalid-email", "age": 16},  # Too short username, invalid email, underage
        {"username": "validuser", "email": "user@domain.com", "age": 17},  # Underage
        {"username": "test", "email": "test@example.com", "age": 20},  # Username too short
    ]

    for i, user_data in enumerate(invalid_users, 1):
        print(f"Testing invalid user {i}: {user_data}")
        try:
            user = UserRegister(**user_data)
            print("User created successfully (unexpected)")
            print("\n" + "="*50 + "\n")
        except ValidationError as e:
            print("\n" + "="*50 + "\n")
            print(f"!!!!!Validation failed: {e}")
        print()
