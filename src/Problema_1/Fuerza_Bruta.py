#Subsecuencia mas larga de un palindromo con Fuerza bruta.

from .usar import normalizar, es_palindromo
from typing import List, Tuple

def subsecuencia_mas_larga_palindromo(c: str) -> Tuple[List[str], int]:
    s = normalizar(c)
    n = len(s)
    max_len = 0
    resultados = set()

    
    for mask in range(1, 1 << n):
        subseq = ''.join(s[i] for i in range(n) if (mask >> i) & 1)
        if es_palindromo(subseq):
            l = len(subseq)
            if l > max_len:
                max_len = l
                resultados = {subseq}
            elif l == max_len:
                resultados.add(subseq)

    return list(resultados), max_len