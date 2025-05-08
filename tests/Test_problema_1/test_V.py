import time
import random
import string
import pytest

from src.Problema_1.Ruta_voraz import subsecuencia_larga_voraz


#Propiedades básicas (juguete)
@pytest.mark.parametrize("input_str", [
    "", "a", "aa", "ab", "ba", "aba", "abac", "racecar"
])
def test_voraz_palindromicity_and_length(input_str):
    subs, length = subsecuencia_larga_voraz(input_str)
    assert isinstance(subs, list) and len(subs) >= 1
    for p in subs:
        assert p == p[::-1]
        assert len(p) == length
    if input_str == "":
        assert length == 0
    else:
        assert length >= 1


# Propiedad en aleatorios 

@pytest.mark.parametrize("n,reps", [
    (10, 5),    
    (50, 3),    
    (100, 2),  
])
def test_voraz_random_palindromicity(n, reps):
    chars = string.ascii_letters + string.digits
    for _ in range(reps):
        s = ''.join(random.choices(chars, k=n))
        subs, length = subsecuencia_larga_voraz(s)
        for p in subs:
            assert p == p[::-1]
            assert len(p) == length


# Rendimiento factible 

@pytest.mark.parametrize("n,max_time", [
    (500,   0.20),   
    (1000,  0.50),   
])
def test_voraz_performance_feasible(n, max_time):
    s = ''.join(random.choices(string.ascii_lowercase, k=n))
    t0 = time.time()
    subs, length = subsecuencia_larga_voraz(s)
    dur = time.time() - t0
    
    assert isinstance(subs, list) and len(subs) >= 1
    for p in subs:
        assert p == p[::-1]
        assert len(p) == length
    
    assert dur < max_time


# Rendimiento no factible 

@pytest.mark.parametrize("n", [5000, 10000, 50000])
@pytest.mark.skip(reason="Voraz no probado para n grandes en CI")
def test_voraz_performance_skip(n):
    subsecuencia_larga_voraz("x"*n)
    s = ''.join(random.choices(string.ascii_lowercase, k=n))
    subsecuencia_larga_voraz(s)
