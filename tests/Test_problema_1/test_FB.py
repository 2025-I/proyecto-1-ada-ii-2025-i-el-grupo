import time
import random
import string
import pytest

from src.Problema_1.Fuerza_Bruta import subsecuencia_mas_larga_palindromo


# 1) Tests de corrección (juguete)

@pytest.mark.parametrize("input_str, expected_subseqs, expected_len", [
    
    ("abac", ["aba"], 3),
    ("Aa", ["aa"], 2),
    ("", [], 0),
])
def test_correctitud_basica(input_str, expected_subseqs, expected_len):
    subs, length = subsecuencia_mas_larga_palindromo(input_str)
    assert length == expected_len
    assert set(subs) == set(expected_subseqs)
    
    for p in subs:
        assert p == p[::-1]


# 2) Tests de rendimiento por tamaños

@pytest.mark.parametrize("n, reps, max_avg", [
    (10,    5,  0.05),  
    (12,    5,  0.20),  
])
def test_perf_pequeno(n, reps, max_avg):
    """Mide fuerza bruta para n pequeños con varias repeticiones."""
    s = ''.join(random.choices(string.ascii_lowercase, k=n))
    times = []
    for _ in range(reps):
        t0 = time.time()
        subsecuencia_mas_larga_palindromo(s)
        times.append(time.time() - t0)
    avg = sum(times) / reps
    print(f"\n[n={n}] avg time over {reps} runs: {avg:.4f}s")
    assert avg < max_avg

@pytest.mark.timeout(5)
@pytest.mark.parametrize("n", [100, 1000, 10_000, 50_000])
def test_perf_grande_xfail(n):
    """
    Test XFAIL para n grandes: la fuerza bruta es exponencial y fallará
    o tardará demasiado; se marca como xfail para documentar que no es factible.
    """
    s = ''.join(random.choices(string.ascii_lowercase, k=n))
    with pytest.raises(TimeoutError) or pytest.xfail(f"Brute force impracticable para n={n}"):
        subsecuencia_mas_larga_palindromo(s)
