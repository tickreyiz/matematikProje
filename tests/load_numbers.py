# tests/load_numbers.py
def load(name):
    with open(f"results/numbers/{name}.txt", "r") as f:
        return [float(line.strip()) for line in f.readlines()]