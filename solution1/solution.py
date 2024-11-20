def strict(func):
    def wrapper(*args, **kwargs):
        types = func.__annotations__
        if type(args[0]) is types['a'] and type(args[1]) is types['b']:
            return func(*args, **kwargs)
        else:
            raise TypeError
    return wrapper

@strict
def sum_two(a: int, b: int) -> int:
    return a + b

# print(sum_two(1, 2))  # >>> 3
# print(sum_two(1, 2.4))  # >>> TypeError