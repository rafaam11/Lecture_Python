# 5번째 문제 - 3

# 2번에서 만든 파일을 읽어 다음과 같은 결과를 만들어라.
# (파일을 한줄씩 읽어 출력하고 마지막에 총 줄수를 출력하라)

with open("5th_problem","r") as file:
    count = 0
    while True:
        line = file.readline()
        if not line:
            break
        count += 1
        print(line)

    print(count)