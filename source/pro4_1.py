# 4번째 문제 - 1

# 사칙연산을 함수로 구현하라

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a // b


a,b = input().split(" ")
a = int(a)
b = int(b)


print("add:  {}".format(add(a,b)))
print("sub:  {}".format(sub(a,b)))
print("mul:  {}".format(mul(a,b)))
print("div:  {}".format(div(a,b)))