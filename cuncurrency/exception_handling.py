import logging

logger = logging.getLogger(__name__)

class InvalidAgeError(Exception):
    pass

class InvalidAmount(Exception):
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


def debt_amt(amount : int):
    try:
        validate_payment(amount)
    except InvalidAmount as e:
        logger.exception(f"payment failed : {e}")
    else:
        print("payment successful")
    finally:
        print("requested transaction transaction completed ")

def validate_payment(amount : int):
    if amount <= 0:
        raise InvalidAmount("amount can't be less than 0")

debt_amt(0)