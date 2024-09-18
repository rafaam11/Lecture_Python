import random

dictionary = {}

while True:
    # 탈출조건
    if len(dictionary) >= 16:
        break

    num = random.randrange(1,46)
    if num in dictionary:
        continue

    dictionary[num] = num
    print(num, end=" ")
print()