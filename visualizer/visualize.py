import seaborn as sns
import matplotlib.pyplot as plt

def load(name):
    with open(f"results/numbers/{name}.txt", "r") as f:
        return [float(line.strip()) for line in f.readlines()]

algorithms = ["lcg", "mersenne", "xorshift", "atmospheric"]
colors = ["steelblue", "tomato", "seagreen", "orange"]

sns.set_theme(style="darkgrid")

fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes = axes.flatten()

for idx, (name, color) in enumerate(zip(algorithms, colors)):
    numbers = load(name)
    ax = axes[idx]

    sns.histplot(
        numbers, 
        ax=ax, 
        color=color, 
        bins=50, 
        stat="density", 
        alpha=0.7,
        edgecolor="white",
        linewidth=0.5
    )

    ax.axhline(y=1.0, color="red", linestyle="--", linewidth=1.2, label="İdeal Düzgün Dağılım")
    ax.set_xlim(0, 1)
    ax.set_xlabel("Değer")
    ax.set_ylabel("Yoğunluk")
    ax.set_title(f"{name.upper()}", fontsize=12, fontweight="bold")
    ax.legend(fontsize=9)

plt.suptitle("Rastgele Sayı Üreticileri — Histogram Karşılaştırması", fontsize=14, fontweight="bold", y=1.02)
plt.tight_layout()
plt.savefig("results/plots/histograms.png", dpi=150, bbox_inches="tight")
plt.show()
