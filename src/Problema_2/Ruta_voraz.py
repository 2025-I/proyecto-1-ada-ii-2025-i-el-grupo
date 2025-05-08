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

def obtener_niveles_arbol(arbol, raiz):
    """Obtiene los niveles del árbol de abajo hacia arriba usando BFS."""
    visitados = set()
    niveles = []
    cola = [(raiz, 0)]  
    
    while cola:
        nodo, nivel = cola.pop(0)
        
        if nodo in visitados:
            continue
            
        visitados.add(nodo)
        while len(niveles) <= nivel:
            niveles.append([])
            
        niveles[nivel].append(nodo)
        
        for hijo in arbol[nodo]:
            if hijo not in visitados:
                cola.append((hijo, nivel + 1))
    
    return niveles
