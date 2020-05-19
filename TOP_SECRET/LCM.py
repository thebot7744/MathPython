def lcm():
    print("Welcome to least common multiple calculator, it will calculate the greatest common factor of any two given"
        "positive integers")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    n1 = num1
    n2 = num2

    while n1 != n2:
        if n1 > n2:
            n1 = n1 - n2
        if n2 > n1:
            n2 = n2 - n1

    lcm = int(num1 * num2/n1)

    print("The least common multiple is " + str(lcm))

while True:
    lcm()
