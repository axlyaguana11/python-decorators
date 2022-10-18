#Arguments in the decorated function

def decorate_sum(func):
    def wrapper(arg1, arg2):
        print(f'Values to sum are: {arg1} and {arg2}.')
        return func(arg1, arg2)
    return wrapper

@decorate_sum
def sum_nums(num_1, num_2):
    return num_1 + num_2

print(sum_nums(7, 9))