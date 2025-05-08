import time
import random
import pytest

from src.Problema_2.Ruta_voraz import fiesta_voraz


# Tests de corrección básicos (juguete)

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
    invited1, total1 = fiesta_voraz(m1, adj1, ratings1)
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
    invited2, total2 = fiesta_voraz(m2, adj2, ratings2)
    assert invited2 == [0,1,0,0,0,1]
    assert total2   == 25


#Independencia y suma correcta 
@pytest.mark.parametrize("m,reps", [
    (10, 5),   
    (50, 3),  
    (100,2),  
])
def test_voraz_independence_and_sum(m, reps):
    for _ in range(reps):

        parents = [None] + [random.randrange(i) for i in range(1, m)]
        adj = [[0]*m for _ in range(m)]
        for i in range(1, m):
            adj[parents[i]][i] = 1
        ratings = [random.randint(0,50) for _ in range(m)]

        invited, total = fiesta_voraz(m, adj, ratings)
        
        assert isinstance(invited, list) and len(invited) == m
        assert set(invited).issubset({0,1})
        assert sum(r * inc for r, inc in zip(ratings, invited)) == total
        for i in range(m):
            if invited[i] == 1:
                for j in range(m):
                    if adj[i][j] == 1:
                        assert invited[j] == 0


# Performance pequeña 
@pytest.mark.parametrize("m,reps,max_avg", [
    (5,  10, 0.005),  
    (10, 5,  0.02),   
    (50, 3,  0.10),   
])
def test_voraz_performance_small(m, reps, max_avg):
    
    adj = [[0]*m for _ in range(m)]
    for i in range(1, m):
        adj[0][i] = 1
    ratings = [random.randint(0,50) for _ in range(m)]

    times = []
    for _ in range(reps):
        t0 = time.time()
        invited, total = fiesta_voraz(m, adj, ratings)
        times.append(time.time() - t0)
    avg = sum(times) / reps
    print(f"[m={m}] greedy DP time: {avg:.4f}s")
    assert avg < max_avg


# Grandes y extra grandes
@pytest.mark.parametrize("m", [1000, 5000, 10000, 50000])
@pytest.mark.xfail(reason="Greedy O(n^2) con matriz no factible para m grandes en CI")
def test_voraz_performance_xfail(m):
    adj = [[0]*m for _ in range(m)]
    for i in range(1, m):
        adj[0][i] = 1
    ratings = [random.randint(0,50) for _ in range(m)]
    fiesta_voraz(m, adj, ratings)
