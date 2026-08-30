
class MyContextManager:

    def __enter__(self) -> None:
        print("enter....")

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        print("exiting........")
        print("Exception type:", exc_type)
        print("Exception value:", exc_value)
        print("Traceback:", traceback)

with MyContextManager() as mc:
    print("something logic is done")
    raise ValueError("Invalid Value")