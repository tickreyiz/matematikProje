# generators/mersenne.py
import numpy as np
from config import SEED, COUNT

def generate():
    rng = np.random.default_rng(SEED)  # <-- aynı seed
    return rng.random(COUNT).tolist()