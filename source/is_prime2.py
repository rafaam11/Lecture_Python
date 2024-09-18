def is_prime(num):
    for i in range(2,num) :
        if num % i == 0:
            return False
    return True

num = int(input('Input number ? '))
mat = []
for i in range(1,num+1):
    if is_prime(i):
        mat.append(i)
print(mat[len(mat)-1])
