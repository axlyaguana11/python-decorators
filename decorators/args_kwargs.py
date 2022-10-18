

def multiply_result(*args_parent):
    def inner_decorator(func):
        def wrapper(*args):
            nums_sum = args
            nums_multiply = sum(args_parent)
            print(f'sum{nums_sum} * {nums_multiply}:')
            return func(*args) * sum(args_parent)
        return wrapper
    return inner_decorator

@multiply_result(3, 4, 5)
def sum_nums(*args):
    return sum(args)

print(sum_nums(1, 2))