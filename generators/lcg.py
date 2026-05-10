# generators/lcg.py
from config import SEED, COUNT

def generate():
    a, c, m = 1664525, 1013904223, 2**32
    x = SEED  # <-- aynı seed
    numbers = []
    for _ in range(COUNT):
        x = (a * x + c) % m
        numbers.append(x / m)
    return numbers