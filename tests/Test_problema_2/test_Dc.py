import time
import random
import pytest

from src.Problema_2.Ruta_dinamica import fiesta_dinamica


# 1) Tests de corrección básicos (juguete)

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
    invited1, total1 = fiesta_dinamica(m1, adj1, ratings1)
    assert invited1 == [0,1,0,0,1]
    assert total1 == 38

    
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
    invited2, total2 = fiesta_dinamica(m2, adj2, ratings2)
    assert invited2 == [0,1,0,0,1,1]
    assert total2 == 33


# 2) Tests de rendimiento pequeños (juguete → pequeño)

@pytest.mark.parametrize("m,reps,max_avg", [
    (5,  10, 0.005),  
    (10,  5,  0.02),  
    (50,  3,  0.10),  
])
def test_dp_performance_small(m, reps, max_avg):
    
    adj = [[0]*m for _ in range(m)]
    for i in range(1, m):
        adj[0][i] = 1
    ratings = [random.randint(0,50) for _ in range(m)]

    times = []
    for _ in range(reps):
        t0 = time.time()
        invited, total = fiesta_dinamica(m, adj, ratings)
        times.append(time.time() - t0)
        
        assert isinstance(invited, list) and len(invited) == m
        assert sum(a*b for a,b in zip(invited, ratings)) == total

    avg = sum(times) / reps
    print(f"[m={m}] avg DP time: {avg:.4f}s")
    assert avg < max_avg


# 3) Tests de rendimiento medianos (mediano → grande)

@pytest.mark.parametrize("m,max_time", [
    (100,  0.50),   
    (500,  1.00),   
])
def test_dp_performance_medium(m, max_time):
    adj = [[0]*m for _ in range(m)]
    for i in range(1, m):
        adj[0][i] = 1
    ratings = [random.randint(0,100) for _ in range(m)]

    t0 = time.time()
    invited, total = fiesta_dinamica(m, adj, ratings)
    dur = time.time() - t0
    
    assert isinstance(invited, list) and len(invited) == m
    assert sum(a*b for a,b in zip(invited, ratings)) == total
    print(f"[m={m}] DP time: {dur:.4f}s")
    assert dur < max_time


# 4) Tamaños grandes y extra grandes (xfail documentado)

@pytest.mark.parametrize("m", [1000, 5000, 10000, 50000])
@pytest.mark.xfail(reason="DP O(n^2) con matriz no factible para m grandes en CI")
def test_dp_performance_xfail(m):
    adj = [[0]*m for _ in range(m)]
    for i in range(1, m):
        adj[0][i] = 1
    ratings = [random.randint(0,100) for _ in range(m)]
    
    fiesta_dinamica(m, adj, ratings)
