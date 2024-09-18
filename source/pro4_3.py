# 4번째 문제 - 3

# 홀수, 짝수가 몇개 있는지 출력하는 프로그램을 재귀함수로 구현하라

def even(x):
    global count_even
    if x == 0:
        return count_even
    elif x % 2 == 1:
        pass
    elif x % 2 == 0:
        count_even += 1

    return even(x-1)
''' # 멘토님이 푸신 방법
def even(x):
    if x == 0:
        return 0
    elif x % 2 == 1:
        return 0 + even(x-1)
    elif x % 2 == 0:
        return 1 + even(x-1)
'''

def odd(x):
    global count_odd
    if x == 0:
        return count_odd
    elif x % 2 == 1:
        count_odd += 1
    elif x % 2 == 0:
        pass

    return odd(x - 1)


count_even = 0
count_odd = 0
x = int(input())
y = even(x)
z = odd(x)


print("짝수 : {}".format(y))
print("홀수 : {}".format(z))









