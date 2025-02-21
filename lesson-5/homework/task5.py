def is_prime(n):
    result = False
    for i in range(2, n):
        if n % i != 0:
            result = True
        else:
            result = False
            break

    return result

n = int(input("Enter a positive number: "))
print(is_prime(n))