# 4번째 문제 - 2

# 0부터 x까지의 합을 재귀함수로 구현하라

def sum_zero_to_x(x) :

    if x == 0 :
        return 0
    else :
        return x + sum_zero_to_x(x-1)


x = int(input())
y = sum_zero_to_x(x)


print("0 ~ {}  : {} ".format(x,y))