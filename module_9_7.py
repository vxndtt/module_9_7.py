def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        if result > 1 and result % result == 0:
            print('Число простое')
        else:
            print('Число составное')
        return result
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)