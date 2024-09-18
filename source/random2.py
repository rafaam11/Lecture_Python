import random

count = 0
b = []

while True:
    a = int(random.random()*44+1)# (0.0 ~ 1.0)*44+1 --> 1 ~ 45
    if a not in b:
        b.append(a)
        count += 1
        print(a,end=" ")
    if count == 45:
        break

