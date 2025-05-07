#Subsecuencuencia mas larga de un palindromo de forma dinamica
from .usar import normalizar
from typing import List, Tuple, Set

def subsecuencia_larga_dinamica(a: str) -> Tuple[List[str], int]:
    
    s = normalizar(a)
    n = len(s)
    if n == 0:
        return [], 0

    
    L = [[0]*n for _ in range(n)]
    for i in range(n):
        L[i][i] = 1
    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i+length-1
            if s[i] == s[j]:
                L[i][j] = 2 if length == 2 else L[i+1][j-1] + 2
            else:
                L[i][j] = max(L[i+1][j], L[i][j-1])

    max_len = L[0][n-1]

    
    def reconstruir(i: int, j: int) -> Set[str]:
        if i > j:
            return {""}
        if i == j:
            return {s[i]}
        results: Set[str] = set()
        if s[i] == s[j]:
            for mid in reconstruir(i+1, j-1):
                results.add(s[i] + mid + s[j])
        else:
            if L[i+1][j] > L[i][j-1]:
                return reconstruir(i+1, j)
            if L[i+1][j] < L[i][j-1]:
                return reconstruir(i, j-1)
            
            return reconstruir(i+1, j) | reconstruir(i, j-1)
        return results

    subseqs = reconstruir(0, n-1)
    return list(subseqs), max_len
