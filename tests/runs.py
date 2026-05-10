# tests/runs_test.py
import numpy as np
from scipy.stats import norm

def load(name):
    with open(f"results/numbers/{name}.txt", "r") as f:
        return [float(line.strip()) for line in f.readlines()]

def runs_test(numbers):
    n = len(numbers)
    # Her sayı medyandan büyük mü küçük mü
    median = np.median(numbers)
    above = [1 if x >= median else 0 for x in numbers]
    
    # Run sayısını hesapla
    runs = 1
    for i in range(1, n):
        if above[i] != above[i-1]:
            runs += 1
    
    n1 = sum(above)
    n2 = n - n1
    
    # Beklenen run sayısı ve standart sapma
    expected = (2 * n1 * n2 / n) + 1
    variance = (2 * n1 * n2 * (2 * n1 * n2 - n)) / (n**2 * (n - 1))
    
    z = (runs - expected) / np.sqrt(variance)
    p = 2 * (1 - norm.cdf(abs(z)))  # iki kuyruklu test
    return z, p

algorithms = ["lcg", "mersenne", "xorshift", "atmospheric"]

import os
os.makedirs("results/stats", exist_ok=True)

with open("results/stats/runs_test.txt", "w") as f:
    for name in algorithms:
        numbers = load(name)
        z, p = runs_test(numbers)
        karar = "BAĞIMSIZ" if p > 0.05 else "ÖRÜNTÜ VAR"
        line = f"{name}: z={z:.4f}, p={p:.4f}, karar={karar}"
        print(line)
        f.write(line + "\n")