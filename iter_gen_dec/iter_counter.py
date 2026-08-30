
class CounterUp:

    def __init__(self, max_num):
        self.current = 1
        self.maximum = max_num

    def __iter__(self):
        return self

    def __next__(self):

        if self.current > self.maximum:
            raise StopIteration

        value = self.current
        self.current += 1
        return value


counter1 = CounterUp(2)

print(next(counter1))
print(next(counter1))