# 6번째 문제 - 1

# If문을 이용하여 예외처리를 하여라.

x = input().split()
y = []


for i in x:

    if i.isidentifier():
        y.append(i)
        x.insert(x.index(i),"X")
        x.remove(i)
    else:
        y.append("X")

print(x)
print(y)

