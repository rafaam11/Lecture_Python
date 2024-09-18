# 피보나치 수열


dictionary = {
    1:1,
    2:1
}

def fibonacci(n):

    if n == 1  or  n == 2:
        return 1

    if n in dictionary:
        return dictionary[n]

    output = fibonacci(n - 1) + fibonacci(n - 2)
    dictionary[n] = output
    return output

print(fibonacci(10))
