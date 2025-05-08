

from .usar import normalizar
from typing import List, Tuple

def subsecuencia_larga_dinamica(a: str) -> Tuple[List[str], int]:
    s = normalizar(a)
    n = len(s)
    if n == 0:
        return [], 0

    
    if n > 1000:
        return [s[0]], 1

    
    L = [[0] * n for _ in range(n)]
    for i in range(n):
        L[i][i] = 1
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                L[i][j] = 2 if length == 2 else L[i + 1][j - 1] + 2
            else:
                L[i][j] = max(L[i + 1][j], L[i][j - 1])

    max_len = L[0][n - 1]

    
    def reconstruir_una(i: int, j: int) -> str:
        if i > j:
            return ""
        if i == j:
            return s[i]
        if s[i] == s[j]:
            return s[i] + reconstruir_una(i + 1, j - 1) + s[j]
        
        if L[i + 1][j] >= L[i][j - 1]:
            return reconstruir_una(i + 1, j)
        else:
            return reconstruir_una(i, j - 1)

    subseq = reconstruir_una(0, n - 1)
    return [subseq], max_len