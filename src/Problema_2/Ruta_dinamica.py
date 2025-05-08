#Fiesta compañia

def supervision_arbol(matrix):
    n = len(matrix)
    arbol = {i: [] for i in range(n)}

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                arbol[i].append(j)
    return arbol

def raiz_encontrada(arbol):
    n = len(arbol)
    pequeño = [False] * n

    for padre in arbol:
        for hijo in arbol[padre]:
            pequeño[hijo] = True
    
    for i in range(n):
        if not pequeño[i]:
            return i
    
    return 0

def fiesta_dinamica(num_empleados, super_matrix, calificacion):
    arbol = supervision_arbol(super_matrix)
    raiz = raiz_encontrada(arbol)

    p = {}
    almacenar = [0] * num_empleados

    def estructura(nodo):
        if nodo in p:
            return p[nodo]
        
        incluir_nodo = calificacion[nodo]
        no_incluir_nodo = 0

        for hijo in arbol[nodo]:
            incluir_nodo += estructura(hijo)[0]

            incluye, no_incluye = estructura(hijo)
            no_incluir_nodo += max(incluye, no_incluye)

        p[nodo] = (no_incluir_nodo, incluir_nodo)
        return p[nodo]
    
    no_incluir_raiz, incluir_raiz = estructura(raiz)
    mas_alto = max(no_incluir_raiz, incluir_raiz)

    def solucion_recostruccion(nodo, incluye_padre):
        if nodo >= num_empleados:
            return
        
        valor_excluido, valor_incluido = p[nodo]

        if incluye_padre:
            almacenar[nodo] = 0
            for hijo in arbol[nodo]:
                solucion_recostruccion(hijo, False)

        else:
            if valor_incluido > valor_excluido:
                almacenar[nodo] = 1
                for hijo in arbol[nodo]:
                    solucion_recostruccion(hijo, True)

            else:
                almacenar[nodo] = 0
                for hijo in arbol[nodo]:
                    solucion_recostruccion(hijo, False)

    if incluir_raiz > no_incluir_raiz:
        almacenar[raiz] = 1
        incluir_padre = True
    else:
        almacenar[raiz] = 0
        incluir_padre = False

    for hijo in arbol[raiz]:
        solucion_recostruccion(hijo, incluir_padre)

    return almacenar, mas_alto