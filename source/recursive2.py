x = int(input())

def f(a) :
    if a == 0 :
        return 0
    elif a%2 == 0 :
        return 1 + f(a-1)
    else :
        return 0 + f(a-1)
def g(a) :
    if a == 0 :
        return 0
    elif a%2 == 1 :
        return 1 + g(a-1)
    else :
        return 0 + g(a-1)

print("짝수 :", f(x))
print("홀수 :", g(x))