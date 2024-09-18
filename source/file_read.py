with open("timestable.txt","r") as file:

    while True:
        ch = file.read(1)
        if not ch:
            break
        if ch.isdigit() == True and int(ch) % 3 == 0:
            print('*', end=" ")
        else:
            print(ch, end=" ")