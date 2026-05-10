# generators/atmospheric.py
import requests
from config import COUNT

def generate():
    # Seed YOK — her seferinde farklı sayılar
    url = f"https://www.random.org/decimal-fractions/?num={COUNT}&dec=10&col=1&format=plain&rnd=new"
    response = requests.get(url)
    return [float(x) for x in response.text.strip().split()]