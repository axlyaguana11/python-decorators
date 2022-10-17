#Pythonic decorators

def make_upper(func):
    def wrapper():
        return func().upper()
    
    return wrapper

@make_upper
def python_greeting():
    return 'hi, i\'m a Python developer!'

print(python_greeting())    