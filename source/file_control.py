with open("timestable.txt","w") as file:

file.write("Times Table\n")

for i in range(1,10):
    for j in range(2,10):
        file.write("{}x{}={:2} ".format(j, i, i * j))
    file.write("\n")


file.close()