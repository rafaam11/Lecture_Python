# 7번째 문제 - 2
'''
1.	사용자에게 6개가 들어있는 리스트를 입력받고(숫자만 받는다)
각 요소의 자료형을 확인하고 int 형이(숫자자료형) 아니라면 int 형으로 변환하여라

2.	사용자에게 6개가 들어있는 리스트를 입력받고 미리 만들어놓은 6개가 들어있는
리스트와 똑같은지 확인하는 프로그램을 만들어라 (숫자만 생각하자)(순서에 유의한다)

3.	랜덤을 이용하여 1 ~ 45 사이의 숫자 6개를 받아 리스트를 만들어라 (중복에 유의한다)

4.	3번에서 받은 리스트와 사용자가 6개의 요소를 받아 만든 리스트를 비교하여 같은지 확인하여라

'''

y = [1,3,5,7,9,11]

x = input().split()
x = list(map(int,x))

print(x)
print(y)

if x == y :
    print('true')
else:
    print('false')

for i in range(len(x)):
    if x[i] == y[i]:
        print("O",end=" ")
    else :
        print("X",end=" ")



