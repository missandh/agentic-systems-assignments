from pydantic import BaseModel, Field, ValidationError, EmailStr, ConfigDict

class AddressModel(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    city: str = Field(..., min_length=3, description="City name")
    pincode: str = Field(..., pattern=r'^\d{6}$', description="6-digit PIN code")

class UserModel (BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    user_id: int = Field(..., description="Unique identifier for the user")
    name: str = Field(..., description="Name must be at least 2 characters long")
    email: EmailStr = Field(..., description="Must be a valid email address")
    age: int = Field(..., ge=18, description="Age must be 18 or older")
    address: AddressModel = Field(..., description="User's address details")
    is_premium: bool = Field(default=False, description="Indicates if the user has a premium account")

# Example usage and validation
if __name__ == "__main__":
    # Valid user data
    try:
        user = UserModel(
            user_id=1,
            name="Alice",
            email="alice@example.com",
            age=25,
            address=AddressModel(city="Bangalore", pincode="560037"),
            is_premium=True
        )
        print("Valid user data:")
        print(user)
    except ValidationError as e:
        print("Validation errors:")
        for error in e.errors():
            print(f" - {error['msg']}")
#User input for invalid data
    print("\n" + "="*50 + "\n")
    invalid_user_data = {
        "user_id": 2,
        "name": "B",
        "email": "invalid-email",
        "age": 17,
        "address": {"city": "NY", "pincode": "12345"},
        "is_premium": False
    }
    
    try:
        user = UserModel(**invalid_user_data)
        print("User created successfully (unexpected)")
    except ValidationError as e:
        print("Validation errors for invalid user data:")
        for error in e.errors():
            print(f" - {error['msg']}")
