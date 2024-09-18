# 6번째 문제 - 2

# Try문을 이용하여 예외처리를 하여라.

x = input().split()
y = []

for i in x:
    try :
        int(i)
        y.append(i)
        x.insert(x.index(i),"X")
        x.remove(i)
    except :
        y.append("X")
        print("예외발생")
    else :
        print("정상작동")


print(x)
print(y)


