#subsecuencia mas larga de un palindromo con ruta voraz.
from .usar import normalizar, es_palindromo

def subsecuencia_larga_voraz(a):
    normalizar_c = normalizar(a)
    n = len(normalizar_c)

    if n == 0:
        return [""], 0

    secuencia_palindromo = set()
    maximo_length = 0

    for centro in range(n):
        palindromo = palindromo_odd(normalizar_c, centro)

        if len(palindromo) > maximo_length:
            secuencia_palindromo.clear()
            secuencia_palindromo.add(palindromo)
            maximo_length = len(palindromo)
        elif len(palindromo) == maximo_length:
            secuencia_palindromo.add(palindromo)
        
        if centro < n -1:
            palindromo = palindromo_even(normalizar_c, centro)

            if len(palindromo) > maximo_length:
                secuencia_palindromo.clear()
                secuencia_palindromo.add(palindromo)
                maximo_length = len(palindromo)
            elif len(palindromo) == maximo_length:
                secuencia_palindromo.add(palindromo)

    for i in range(n):
        for j in range(i + 1, n):

            if normalizar_c[i] == normalizar_c[j]:
                palindromo = palindromo_voraz(normalizar_c, i, j)

                if len(palindromo) > maximo_length:
                    secuencia_palindromo.clear()
                    secuencia_palindromo.add(palindromo)
                    maximo_length = len(palindromo)
                elif len(palindromo) == maximo_length:
                    secuencia_palindromo.add(palindromo)
    return list(secuencia_palindromo), maximo_length