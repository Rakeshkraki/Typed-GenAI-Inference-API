class InvalidAgeError(Exception):
    pass

def validate_age(age: int):
    try:
        if age < 18:
            raise InvalidAgeError("Age must be greater than or equal to 18")
        print(f"this is age {age}")
    except InvalidAgeError:
        print("must be greater than 18")

validate_age(10)

def multiple_exception() -> None:
    try:
        x = int(input("Enter number: "))
        result = 10 / x
    except ValueError:
        print("Enter a valid number")
    except ArithmeticError:
        print("Cannot divide by zero")
    else:
        print(f"result {result}")
    finally:
        print("running completed...")
