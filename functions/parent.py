#Funtions into functions

def parent():
    print('This is parent function.')
    
    def inner_1():
        print('This is inner function 1.')
    
    def inner_2():
        print('This is inner function 2.')
    
    inner_1()
    inner_2()

parent()

