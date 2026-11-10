# First example
import math

def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)

def hypotenuese(a, b):
    math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return b / a

def logarithim(a, b):
    if b <= 0:
        raise ValueError
    return math.log(b, a)

def exp(a, b):
    return a ** b

