import math


def add(a, b):
    return a + b


def divide(a, b):
    return a / b


def average(numbers):
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    return total / len(numbers)


def sqrt(x):
    return math.sqrt(x)


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False