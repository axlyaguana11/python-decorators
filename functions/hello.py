def hello(name):
    return 'Hello, {name}!'.format(name=name)

#Assign functions to variables

hola = hello
print(hola)
print(hola('Axel'))