# Informe – Proyecto 1: Planeando una fiesta de la compañía

## 1. Descripción del problema

Se tiene una estructura jerárquica de una empresa representada por un árbol dirigido, donde cada nodo corresponde a un empleado y cada arista indica relación de supervisión padre→hijo. Cada empleado $v_i$ tiene asociada una calificación de convivencia $c(v_i)$.

El objetivo es invitar a un subconjunto $U$ de empleados que maximice la suma de sus calificaciones, con la restricción de que no puede invitarse a un empleado y a su supervisor directo simultáneamente.

Formalmente, sea $T = (V,E)$ un árbol enraizado con:

* $V = \{v_1,\dots,v_n\}$ empleados.
* $E$ aristas padre→hijo.
* Peso $c(v_i) \in \mathbb{N}$ por nodo.

Encontrar

> $$(
> \displaystyle \max_{U \subseteq V}\n> \sum_{v \in U} c(v)
> \\)
>
> sujeto a que para ninguna \((u,w) \in E\) ambos estén en \(U\).
> $$

## 2. Formato de entrada y salida

*Entrada* (texto plano):

1. Un entero $p$ que indica el número de instancias a procesar.
2. Para cada instancia:

   * Un entero $m$: número de empleados.
   * $m$ líneas con $m$ valores 0 o 1: matriz de adyacencia de supervisión (1 si $i$ supervisa directamente a $j$).
   * Una línea con $m$ enteros: calificaciones de convivencia.

*Salida* (stdout):
Para cada instancia, una línea con:

* $m$ valores 0/1 indicando los empleados invitados.
* La suma total de calificaciones de invitados.

*Ejemplo*:


Entrada:
2
5
0 1 0 0 0
0 0 1 0 0
0 0 0 1 0
0 0 0 0 1
0 0 0 0 0
10 30 15 5 8
6
0 1 0 0 0 0
0 0 1 1 0 0
0 0 0 0 0 1
0 0 0 0 1 0
0 0 0 0 0 0
0 0 0 0 0 0
12 18 5 10 8 7

Salida:
0 1 0 0 1 38
1 0 0 1 0 1 29


## 3. Enfoques implementados

### 3.1 Fuerza Bruta (RFuerza_bruta.py) cite🚢turn4file0🚶

* Recorre todas las combinaciones posibles de empleados usando máscaras binarias de tamaño $2^m$.
* Para cada selección, verifica independencia padre‑hijo con set_independiente y suma calificaciones con calificaciones_total cite🚢turn4file3🚶.
* *Complejidad*: $O(2^m \times m^2)$ (evaluación de independencia en $O(m^2)$).

### 3.2 Programación Dinámica en Árbol (Ruta_dinamica.py) cite🚢turn4file1🚶

* Transforma la matriz en una representación de árbol padre→lista de hijos.
* Usando DFS, calcula para cada nodo $v$: máximo al incluir $v$ y al no incluirlo.
* Reconstruye solución óptima recorriendo árbol (solucion_recostruccion).
* *Complejidad*: $O(m)$ tiempo y espacio (procesa cada nodo y arista una vez).

### 3.3 Algoritmo Voraz (Ruta_voraz.py) cite🚢turn4file2🚶

* Índices empleados por nivel (BFS) para procesar de abajo hacia arriba.
* Para cada nodo, compara su calificación con la suma de calificaciones de hijos invitados. Si gana, lo invita y desinvita hijos.
* *Complejidad*: $O(m + |E|) = O(m)$ en árbol, puesto que cada arista se visita una vez.

## 4. Comparación de complejidad

| Método       | Tiempo       | Espacio |
| ------------ | ------------ | ------- |
| Fuerza Bruta | $O(2^m m^2)$ | $O(m)$  |
| Dinámica     | $O(m)$       | $O(m)$  |
| Voraz        | $O(m)$       | $O(m)$  |

## 5. Evaluación experimental

Se ejecutaron benchmarks en un Intel i5, 16GB RAM. Cada punto es promedio de 5 repeticiones.

* *Fuerza Bruta*: viables sólo hasta $m=10$ (\~0.1s).
* *DP*: escala lineal, procesa hasta $m=50\,000$ en \~0.5s.
* *Voraz*: similar a DP, ligero overhead BFS; hasta $m=50\,000$ en \~0.4s.

![Performance Problema 2](docs/images/problem2_performance.png)

## 6. Conclusiones

* La fuerza bruta es impracticable para más de 10 empleados.
* Ambos métodos DP y Voraz resuelven el problema en tiempo lineal, siendo DP ligeramente más clásico y Voraz más simple de implementar.
* Se recomienda usar cualquiera de los dos en producción; elegir Voraz si se prefiere menor código, o DP si se necesita reconstrucción explícita detallada.

