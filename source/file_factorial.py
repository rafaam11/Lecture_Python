def get_factorial(num):
    a = 1
    for i in range(1,num+1):
        a = a * i
    return a

ppap = input("Input filename ? ")
num_box = []
sum = 0
with open(ppap,"r") as file:

    while True:
        ch = file.read(1)
        if not ch:
            break
        if ch.isdigit() == True:
           num_box.append(ch)

for i in range(0,len(num_box)):
    print("{}!".format(num_box[i]), end=" ")
    int_number = int(num_box[i])
    sum += get_factorial(int_number)
print("={}".format(sum))





