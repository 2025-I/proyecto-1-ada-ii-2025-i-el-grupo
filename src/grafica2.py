import sys
import os
import random
import time
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.abspath("src"))

from Problema_2.Ruta_dinamica import fiesta_dinamica
from Problema_2.Ruta_voraz import fiesta_voraz

def generate_tree(n):
    adj = [[0] * n for _ in range(n)]
    for i in range(1, n):
        parent = random.randint(0, i - 1)
        adj[parent][i] = 1
    return adj

def generate_ratings(n, low=1, high=100):
    return [random.randint(low, high) for _ in range(n)]

def benchmark_and_plot(sizes, reps=5):
    dp_times = []
    voraz_times = []

    for n in sizes:
        dp_run_times = []
        voraz_run_times = []
        for _ in range(reps):
            tree = generate_tree(n)
            ratings = generate_ratings(n)

            t0 = time.perf_counter()
            fiesta_dinamica(n, tree, ratings)
            dp_run_times.append(time.perf_counter() - t0)

            t0 = time.perf_counter()
            fiesta_voraz(n, tree, ratings)
            voraz_run_times.append(time.perf_counter() - t0)

        dp_avg = sum(dp_run_times) / reps
        voraz_avg = sum(voraz_run_times) / reps
        print(f"n={n}: DP avg={dp_avg:.4f}s, Voraz avg={voraz_avg:.4f}s")

        dp_times.append(dp_avg)
        voraz_times.append(voraz_avg)

    
    theo_dp = [n * 1e-6 for n in sizes]        
    theo_voraz = [n**2 * 1e-8 for n in sizes]  

    plt.plot(sizes, dp_times, marker='o', label="DP (experimental)")
    plt.plot(sizes, voraz_times, marker='x', label="Voraz (experimental)")
    plt.plot(sizes, theo_dp, '--', label="DP O(n) teórico")
    plt.plot(sizes, theo_voraz, '--', label="Voraz O(n²) teórico")

    plt.xlabel("Número de empleados (n)")
    plt.ylabel("Tiempo promedio (s)")
    plt.title("Problema 2: Rendimiento DP vs Voraz")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    test_sizes = [100, 500, 800, 1000, 1500, 2000, 5000, 10000]
    benchmark_and_plot(test_sizes)
