def greater_first(func):
    def swap(a, b):
        if a < b:
            a, b = b, a
        return func(a,b)
    return swap

@greater_first
def div(a: int, b: int) -> float:
    return a / b


@greater_first
def sub(a: int, b: int) -> int:
    return a - b

print(div(1,5))

print(sub(2, 20))