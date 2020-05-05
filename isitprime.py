import math

check = True

"""this is where we set up the number"""
Ask = input("Enter a number: ")
num = int(Ask)
divnum = math.sqrt(num)
wherediv = round(divnum)
isprime = True

# print(wherediv)      just for debug purposes

while check and wherediv > 1:
    if num % wherediv == 0:
        what_is_it = int(num / wherediv)
        print("Your number is composite. It can be divided by " + str(what_is_it) + " and " + str(wherediv))
        isprime = False
        check = False
    else:
        wherediv = wherediv - 1
#        print(wherediv)
if isprime:
    print("Your number is prime.")
