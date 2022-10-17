#Returning another function

def choose_num(num):
    def opt_1():
        return 'You choose 9.'

    def opt_2():
        return 'You didn\'t choose 9.'

    if num == 9:
        return opt_1

    else:
        return opt_2

option_1 = choose_num(9)
option_2 = choose_num(2)

print(option_1) #prints the class
print(option_1()) #prints the returned string