from collections import Counter
from itertools import product
from random import randint
from math import factorial as fact

# Находим все простые делители
def get_prime_divisors(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            n //= i
            yield i
        else:
            i += 1
    if n > 1:
        yield n


# Считаем произведение элементов из каждой комбинации
def calc_product(iterable):
    acc = 1
    for i in iterable:
        acc *= i
    return acc


# Находим все делители
def get_all_divisors(n):
    primes = get_prime_divisors(n)
    primes_counted = Counter(primes)
    # Возводим каждый простой делитель в степень и заполняем массив
    divisors_exponentiated = [
        [div ** i for i in range(count + 1)] for div, count in primes_counted.items()
    ]
    # Комбинируем все степени простых делителей и отправляем не перемножение в функцию выше
    for prime_exp_combination in product(*divisors_exponentiated):
        yield calc_product(prime_exp_combination)


num = randint(5, 15)
print(list(get_all_divisors(fact(num))))
