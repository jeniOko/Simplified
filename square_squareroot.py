import math

#square
def square(number):
    return number * number

#squareroot
def square_root(number):
   return math.sqrt(number)

number = (float(input("ENTER A NUMBER : ")))
act = input("S for Square and R for Square root: ")


if act.upper() == 'S':
    print(square(number))
elif act.upper() == 'R':
    print(square_root(number))
else:
    print('RELOAD!! Please use S or R for square or square root respectively, to get results ')
