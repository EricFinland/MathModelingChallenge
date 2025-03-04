# Re-import necessary libraries after execution state reset
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

def h(x):
    return 18 * np.cos((np.pi / 12) * x) + 56

def a_function(x):
    return 9.5 * 0.01 * h(x) * 0.7833222483

def f(x, a):
    return -a * np.cos((np.pi / 12) * (x - 2)) + 81.25

x_values = np.linspace(0, 24, 1000)

variation_factors = [0.94, 0.96, 0.98, 1.00, 1.02, 1.04, 1.06]
a_variations = [a_function(x_values) * factor for factor in variation_factors]

colors = ['purple', 'red', 'orange', 'blue', 'green', 'darkgreen', 'black']
labels = [f"{(factor - 1) * 100:.1f}% Change" for factor in variation_factors]

plt.figure(figsize=(10, 6))

base_y_values = f(x_values, a_variations[3])  

for i, (a_values, color, label) in enumerate(zip(a_variations, colors, labels)):
    y_values = f(x_values, a_values)
    plt.plot(x_values, y_values, alpha=0.7, color=color, linewidth=1, label=label)
    
    if i == 0 or i == 6:  
        r2 = r2_score(base_y_values, y_values)
        print(f"R² value for {labels[i]}: {r2:.4f}")

plt.xlabel("x (Time, 0 to 24)")
plt.ylabel("f(x) (Function Output)")
plt.title("Sensitivity Analysis of f(x) with ±4% to ±6% Variation in a")
plt.legend()
plt.grid(True)
plt.show()
