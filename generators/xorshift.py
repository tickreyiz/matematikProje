# generators/xorshift.py
from config import SEED, COUNT

def generate():
    x = SEED  # <-- aynı seed
    numbers = []
    for _ in range(COUNT):
        x ^= (x << 13) & 0xFFFFFFFF
        x ^= (x >> 17) & 0xFFFFFFFF
        x ^= (x << 5)  & 0xFFFFFFFF
        numbers.append(x / 0xFFFFFFFF)
    return numbers