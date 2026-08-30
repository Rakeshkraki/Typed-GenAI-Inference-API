#
# Create one
#    ↓
# Process one
#    ↓
# Create next
#    ↓
# Process next

def get_numbers():
    yield 1
    yield 2


nums = get_numbers()
print(next(nums))
print(next(nums))


# list vs generator

# List:
#
# 1 2 3 4 5 6 ... 999999
# └─────────────── memory ───────────────┘
#
#
# Generator:
#
# current state
#      ↓
#    value


def get_numbers_list():
    return [i for i in range(1_000_000)]

def get_numbers_generator():
    for i in range(1_000_000):
        yield i

nums_gen = (print(x * 2) for x in range(1,5))

next(nums_gen)
next(nums_gen)
next(nums_gen)