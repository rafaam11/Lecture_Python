count = 0
while True :
    try :
        num = int(input("Input number ? "))

        if num % 2 == 0:
            print("{} is even number".format(num))
        else :
            print("{} is odd number".format(num))

    except :
        print("Processing error")

    else :
        print("Processing okay")
    finally :
        count += 1
        print("Finally, loop count {}".format(count))
