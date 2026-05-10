# generate_all.py
import os
from generators import lcg, mersenne, xorshift

os.makedirs("results/numbers", exist_ok=True)


for name, func in [("lcg", lcg.generate), ("mersenne", mersenne.generate),
                   ("xorshift", xorshift.generate)]:
    numbers = func()
    with open(f"results/numbers/{name}.txt", "w") as f:
        f.write("\n".join(map(str, numbers)))
    print(f"{name}: {len(numbers)} sayı kaydedildi.")