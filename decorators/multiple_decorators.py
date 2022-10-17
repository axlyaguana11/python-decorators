#Multiple decorators

def make_upper(func):
    def wrapper():
        return func().upper()
    
    return wrapper

def reverse_str(func):
    def wrapper():
        return func()[::-1] 
    
    return wrapper   

@make_upper
@reverse_str
def python_greeting():
    return 'hi, i\'m a Python developer!'

print(python_greeting())    