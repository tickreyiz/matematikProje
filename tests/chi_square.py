# tests/chi_square.py
from scipy.stats import chisquare
import numpy as np
from load_numbers import load

def run(name):
    numbers = load(name)
    k = 10  # 10 eşit aralık
    observed, _ = np.histogram(numbers, bins=k, range=(0, 1))
    expected = [len(numbers) / k] * k
    stat, p = chisquare(observed, expected)
    return stat, p

algorithms = ["lcg", "mersenne", "xorshift", "atmospheric"]

with open("results/stats/chi_square.txt", "w") as f:
    for name in algorithms:
        stat, p = run(name)
        karar = "DÜZGÜN" if p > 0.05 else "DÜZGÜN DEĞİL"
        line = f"{name}: chi2={stat:.4f}, p={p:.4f}, karar={karar}"
        print(line)
        f.write(line + "\n")