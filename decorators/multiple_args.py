#Arguments in decorator and decorated function

def multiply_result(num_3):
    def inner_decorator(func):
        def wrapper(arg1, arg2):
            print(f'({arg1} + {arg2}) * {num_3}:')
            return func(arg1, arg2) * num_3 
        return wrapper
    return inner_decorator

@multiply_result(3)
def sum_nums(num_1, num_2):
    return num_1 + num_2

print(sum_nums(1, 2))