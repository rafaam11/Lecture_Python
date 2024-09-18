
def is_prime(num):

    for i in range(2,num) :
        if num % i == 0:
            return False

    return True

num = int(input('Input number ? '))

if is_prime(num) == True :
    print("{} is prime number".format(num))

else :
    print("{} is not prime number".format(num))
