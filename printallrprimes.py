"""This is someone else's program."""

lower = int(input("What is the lower limit: "))
higher = int(input("What is the upper limit: "))
for num in range(lower,higher + 1):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            print(num)
