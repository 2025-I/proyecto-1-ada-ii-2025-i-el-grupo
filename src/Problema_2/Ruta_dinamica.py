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