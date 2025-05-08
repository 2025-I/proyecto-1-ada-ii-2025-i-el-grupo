import time
import random
import string
import pytest

from src.Problema_1.Ruta_dinamica import subsecuencia_larga_dinamica


#Tests de corrección básicos (juguete)

@pytest.mark.parametrize("input_str, expected_len", [
    ("",       0),
    ("a",      1),
    ("aa",     2),
    ("ab",     1),
    ("aba",    3),
    ("abac",   3),
    ("AaBbA",  4),  
])
def test_dp_basic(input_str, expected_len):
    subs, length = subsecuencia_larga_dinamica(input_str)
    assert length == expected_len
    for p in subs:
        assert p == p[::-1]
        assert len(p) == length


#Tests de rendimiento 

@pytest.mark.parametrize("n,reps,max_avg", [
    (10,    5,   0.05),   
    (100,   3,   0.10),   
    (500,   2,   0.30),   
    (1000,  1,   1.00),   
])
def test_dp_performance(n, reps, max_avg):
    """Mide tiempo medio de subsecuencia_larga_dinamica para distintos tamaños."""
    chars = string.ascii_letters + string.digits
    s = ''.join(random.choices(chars, k=n))
    times = []
    for _ in range(reps):
        t0 = time.time()
        subs, length = subsecuencia_larga_dinamica(s)
        times.append(time.time() - t0)
        assert all(p == p[::-1] for p in subs)
        assert all(len(p) == length for p in subs)
    avg = sum(times) / reps
    print(f"\n[n={n}] avg DP time over {reps} runs: {avg:.4f}s")
    assert avg < max_avg



#Tamaños extra grandes

@pytest.mark.parametrize("n", [5000, 10000, 50000])
def test_dp_extra_large(n):
    """Ahora debe pasar para todos los tamaños sin colgar el CI."""
    s = ''.join(random.choices(string.ascii_lowercase, k=n))
    subs, length = subsecuencia_larga_dinamica(s)
    assert all(p == p[::-1] for p in subs)
    assert length >= 1