# Informe – Problema_1 1: Subsecuencias más largas de un palíndromo

## 1. Descripción del problema

Dada una cadena de caracteres $S$, se desea encontrar todas las subsecuencias palindrómicas de máxima longitud, ignorando:

* Diferencias entre mayúsculas y minúsculas.
* Caracteres no alfanuméricos (espacios, puntuación, etc.).

Formalmente, sea $Σ$ un alfabeto y $S = s_1 s_2 \dots s_n ∈ Σ^*$. Definimos la normalización:

* $ϕ(c) = $ minúscula(c) si $c$ es alfanumérico;
* $ϕ(c) = ε$ en otro caso;

Sea $S' = ϕ(s_1)ϕ(s_2)\dots ϕ(s_n)$. Una subsecuencia palindrómica $P$ de $S'$ satisface:

> $P = p_1 p_2 \dots p_k$, con índices $1 ≤ i_1 < i_2 < \dots < i_k ≤ n$,
>
> $p_j = s'_{i_j}$ y $P = \\text{reverse}(P)$.

Buscamos:

> $$(
> \displaystyle \max_{P ∈ \mathcal P} |P|,
> \\)
> $$

donde $\mathcal P$ es el conjunto de todas las subsecuencias palindrómicas de $S'$.

## 2. Formato de entrada y salida

**Entrada**: Un archivo de texto con:

1. Una línea con un entero $n$: número de cadenas.
2. Siguientes $n$ líneas: cada cadena original.

**Salida** (stdout): $n$ líneas, cada una con las subsecuencias palindrómicas de máxima longitud, en minúsculas, separadas por espacio si hay varias.

**Ejemplo**:

```
Entrada:
3
Llego a tierra y le dijo: Dabale arroz a la zorra el abad, ella aceptó
El ministro dijo Se es o no se es un ministro
Maria dijo Yo dono rosas, oro no doy por ello el la dejo

Salida:
dabalearrozalzorraelabad
seesonoses
yonodonorosasoronodoy
```

## 3. Normalización de la cadena

Se implementó en `usar.py`:

```python
import unicodedata

def normalizar(cadena):
    cadena = cadena.lower()
    return ''.join(c for c in cadena if c.isalnum())

def es_palindromo(cadena):
    return cadena == cadena[::-1]
```

## 4. Enfoques implementados

### 4.1 Fuerza Bruta (`Fuerza_Bruta.py`) ✨

* Recorre todas las subsecuencias posibles mediante un *bitmask* de tamaño $2^n-1$.
* Para cada subsecuencia, comprueba si es palíndromo y actualiza el máximo.
* **Complejidad temporal**: $O(2^n · n)$.
* **Uso de memoria**: $O(2^n)$ en el peor caso (almacenamiento del conjunto de resultados).

### 4.2 Programación Dinámica (`Ruta_dinamica.py`) 🚀

* Construye una tabla $L[i][j]$ con la longitud de la LPS (Longest Palindromic Subsequence) para cada subcadena $s[i..j]$.
* Reconstruye recursivamente todas las subsecuencias de longitud máxima.
* **Complejidad temporal**: $O(n^2)$ para llenar la tabla + coste adicional de reconstrucción (depende del número de soluciones).
* **Complejidad espacial**: $O(n^2)$.

### 4.3 Algoritmo Voraz (`Ruta_voraz.py`) 🍃

* Expande palíndromos centrados en cada posición (odd/even) en tiempo $O(n^2)$.
* Además, explora pares de coincidencias con heurística voraz, en $O(n^3)$ en el peor caso.
* **Complejidad temporal**: $O(n^3)$.
* **Complejidad espacial**: $O(1)$ extra.

## 5. Análisis de complejidad teórica

| Método       | Tiempo          | Espacio  |
| ------------ | --------------- | -------- |
| Fuerza Bruta | $O(2^n · n)$    | $O(2^n)$ |
| Dinámica     | $O(n^2)$        | $O(n^2)$ |
| Voraz        | $O(n^3)$ (peor) | $O(1)$   |

## 6. Evaluación experimental

Se realizaron pruebas de corrección y rendimiento utilizando `pytest` con marcadores de parametrización y `time.perf_counter()`. Además, se generaron gráficas de rendimiento:

* **Brute Force**: casos juguete $n=10,12,14$ tardan milisegundos.
* **Programación Dinámica**: prueba hasta $n=1000$ en tiempos razonables (<1s).
* **Voraz**: prueba hasta $n=10000$ (<2s) antes de marcar XFAIL para tamaños mayores.


## 7. Conclusiones

* La **fuerza bruta** es inviable para cadenas largas (crecimiento exponencial).
* La **programación dinámica** ofrece un buen equilibrio para $n$ hasta miles, con un tiempo polinómico y espacio cuadrático.
* El **método voraz**, aunque conceptualmente rápido, en el peor caso llega a $O(n^3)$, por lo que sólo es práctico para tamaños moderados.


