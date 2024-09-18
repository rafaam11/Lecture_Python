# 5번째 문제 - 2

# 파일입출력을 이용하여 결과를 다음과 같이 저장하라.

with open("5th_problem","w") as file:
    x = int(input())
    for i in range(1,x+1):
        if i % 2 == 1:
            file.write("1 \n")
        else :
            file.write("0 \n")

