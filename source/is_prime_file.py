def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False

    return True

with open("prime_numbers.txt","w") as file:

    a = int(input("Input start number ? "))
    b = int(input("Input number count ? "))
    count = 0
    while True :
        if is_prime(a) == True :
            file.write("{},".format(a))
            count += 1
        a += 1
        if count == b:
            break
