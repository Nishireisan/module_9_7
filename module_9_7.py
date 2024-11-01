
def is_prime(func):
    def wrapper(*args):
        f = 0
        result = func(*args)
        for i in range(result):
            if result % (i+1) == 0:
                f += 1
        if f >= 2:
            print('Простое')
            return result
        else:
            print('Составное')
            return result
    return wrapper

@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)
