#Functions as arguments

def duplicate(num):
    return num * 2

def test_function(func):
    num_2_duplicate = 13
    return func(num_2_duplicate)

print(test_function(duplicate))
