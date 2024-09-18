def space(num):
    while num > 0:
        n = len(str(num)) - 1
        a = 10**n
        se = num//a
        print("{}".format(se), end=" ")
        return space(num - se*a)


num = int(input("Input number ? "))
space(num)