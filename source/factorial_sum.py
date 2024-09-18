def get_factorial(num):
    a = 1
    for i in range(1,num+1):
        a = a * i
    return a


num1 = int(input("Input number 1 ? "))
num2 = int(input("Input number 2 ? "))
sum = 0
for i in range(num1,num2):
    print("1/{}!+".format(i),end="")
    sum = sum + 1/get_factorial(i)
sum = sum + 1/get_factorial(num2)
print("1/{}!={}".format(num2,sum))


