#Debugging

import functools

#Uncomment the following code and see the difference respect to that not commented.

# def make_upper(func):
#     def wrapper():
#         """Wrapper function"""
#         return func().upper()
    
#     return wrapper

# @make_upper
# def python_greeting():
#     """Python greeting function"""
#     return 'hi, i\'m a Python developer!'

# print(python_greeting.__name__)
# print(python_greeting.__doc__)


# Decorators with debugging

def make_upper(func):
    @functools.wraps(func)  #This decorator changes the debugging rules UwU
    def wrapper():
        """Wrapper function"""
        return func().upper()
    
    return wrapper

@make_upper
def python_greeting():
    """Python greeting function"""
    return 'hi, i\'m a Python developer!'

print(python_greeting.__name__)
print(python_greeting.__doc__)