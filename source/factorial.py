
def get_factorial(num):
    a = 1
    for i in range(1,num+1):
        a = a * i
    return a

num = int(input("input number ? "))
sum = 0
for i in range(1,num+1):
    sum = sum + get_factorial(i)
    if i == num :
        print("{}! = ".format(i),end=" ")
    else :
        print("{}! + ".format(i),end="")
print(sum)

