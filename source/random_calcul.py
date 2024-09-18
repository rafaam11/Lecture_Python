import random


while True:
    num1 = random.randrange(0,10)
    num2 = random.randrange(0,10)
    giho = random.choice(["+","-","*","/"])

    answer = input("{} {} {} = ? ".format(num1,giho,num2))
    if answer == "exit":
        break

    if giho == "+":
        ans = num1 + num2
    elif giho == "-":
        ans = num1 - num2
    elif giho == "*":
        ans = num1 * num2
    else:
        ans = num1 / num2

    if answer == ans:
        print("Correct")
    else:
        print("Wrong! Answer = {}".format(ans))








