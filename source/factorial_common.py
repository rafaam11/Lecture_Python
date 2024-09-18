
def get_factorial(num):
    a = 1
    for i in range(1,num+1):
        a = a * i
    return a

num = int(input("input number ? "))

print(get_factorial(num))