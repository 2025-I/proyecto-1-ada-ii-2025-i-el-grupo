import time
import random
import pytest

from src.Problema_2.RFuerza_bruta import compañia_fuerza_bruta

# ——————————————————————————————
# 1) Tests de corrección básicos (juguete)
# ——————————————————————————————
def test_basic_examples():
    m1 = 5
    adj1 = [
        [0,1,0,0,0],
        [0,0,1,0,0],
        [0,0,0,1,0],
        [0,0,0,0,1],
        [0,0,0,0,0],
    ]
    ratings1 = [10,30,15,5,8]
    invited1, total1 = compañia_fuerza_bruta(m1, adj1, ratings1)
    assert invited1 == [0,1,0,0,1]
    assert total1   == 38

    m2 = 6
    adj2 = [
        [0,1,0,0,0,0],
        [0,0,1,1,0,0],
        [0,0,0,0,0,1],
        [0,0,0,0,1,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
    ]
    ratings2 = [12,18,5,10,8,7]
    invited2, total2 = compañia_fuerza_bruta(m2, adj2, ratings2)
    assert invited2 == [0,1,0,0,1,1]
    assert total2   == 33

# ——————————————————————————————
# 2) Tests de rendimiento (juguete → pequeño)
# ——————————————————————————————
@pytest.mark.parametrize("m,reps,max_avg", [
    (5,  10, 0.005),   
    (10,  5, 0.02),    
])
def test_bf_performance_small(m, reps, max_avg):
    adj = [[0]*m for _ in range(m)]
    for i in range(1, m):
        adj[0][i] = 1
    ratings = [random.randint(0,50) for _ in range(m)]

    times = []
    for _ in range(reps):
        t0 = time.time()
        compañia_fuerza_bruta(m, adj, ratings)
        times.append(time.time() - t0)
    avg = sum(times)/reps
    print(f"\n[m={m}] brute avg: {avg:.4f}s")
    assert avg < max_avg

# ——————————————————————————————
# 3) Tamaños grandes y extra grandes (xfail documentado)
# ——————————————————————————————
@pytest.mark.parametrize("m", [20, 50, 100, 500, 1000, 50000])
@pytest.mark.xfail(reason="Fuerza bruta exponencial: no factible para m > 10 en CI")
def test_bf_large_xfail(m):
    adj = [[0]*m for _ in range(m)]
    for i in range(1, m):
        adj[0][i] = 1
    ratings = [random.randint(0,50) for _ in range(m)]
    compañia_fuerza_bruta(m, adj, ratings)
