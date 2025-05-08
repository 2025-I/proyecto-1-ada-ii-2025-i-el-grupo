import sys
import os
import random
import time
import matplotlib.pyplot as plt


sys.path.insert(0, os.path.abspath("src"))

from Problema_1.Fuerza_Bruta import subsecuencia_mas_larga_palindromo
from Problema_1.Ruta_dinamica import subsecuencia_larga_dinamica
from Problema_1.Ruta_voraz import subsecuencia_larga_voraz

def generate_string(n):
    """Genera una cadena alfanumérica aleatoria de longitud n."""
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
    return "".join(random.choices(alphabet, k=n))

def benchmark_and_plot(sizes, reps=5):
    bf_times = []
    dp_times = []
    voraz_times = []

    for n in sizes:
        t_bf, t_dp, t_vz = [], [], []
        for _ in range(reps):
            s = generate_string(n)

            
            t0 = time.perf_counter()
            subsecuencia_mas_larga_palindromo(s)
            t_bf.append(time.perf_counter() - t0)

            
            t0 = time.perf_counter()
            subsecuencia_larga_dinamica(s)
            t_dp.append(time.perf_counter() - t0)

            
            t0 = time.perf_counter()
            subsecuencia_larga_voraz(s)
            t_vz.append(time.perf_counter() - t0)

        avg_bf = sum(t_bf) / reps
        avg_dp = sum(t_dp) / reps
        avg_vz = sum(t_vz) / reps
        print(f"n={n}: BF avg={avg_bf:.4f}s, DP avg={avg_dp:.4f}s, Voraz avg={avg_vz:.4f}s")

        bf_times.append(avg_bf)
        dp_times.append(avg_dp)
        voraz_times.append(avg_vz)

    
    theo_dp = [n**2 * 1e-8 for n in sizes]  
    theo_vz = [n * 1e-6 for n in sizes]     

    plt.plot(sizes, bf_times, marker='.', label="FuerzaBruta (exp)")
    plt.plot(sizes, dp_times, marker='o', label="DP (exp)")
    plt.plot(sizes, voraz_times, marker='x', label="Voraz (exp)")
    plt.plot(sizes, theo_dp, '--', label="DP O(n²) teórico")
    plt.plot(sizes, theo_vz, '--', label="Voraz O(n) teórico")

    plt.xlabel("Longitud de la cadena (n)")
    plt.ylabel("Tiempo medio (s)")
    plt.title("Problema 1: Rendimiento vs Tamaño")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    
    test_sizes = [10, 12, 14, 16, 18, 20, 22]
    benchmark_and_plot(test_sizes)
