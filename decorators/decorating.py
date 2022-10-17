#Decorator

def make_upper(func):
    def wrapper():
        return func().upper()
    
    return wrapper


def python_greeting():
    return 'hi, i\'m a Python developer!'

python_greeting = make_upper(python_greeting)  #This is what decorates the function

print(python_greeting())
print(python_greeting)