import random

True_number = random.randrange(1,100)
# print(True_number)
count = 0

while True:
    count += 1
    num = int(input("Guess number ? "))
    if num == True_number:
        print("Correct! total {} times".format(count))
        break
    if num > True_number :
        print("Down")
    if num < True_number :
        print("Up")

