#Fiesta compañia

def lee_datos(linea, inicio):
    num_empleados = int(linea[inicio].strip())
    matriz_supervizor = []

    for i in  range(inicio + 1, inicio + 1 + num_empleados):
        fila = list(map(int, linea[i].strip().split()))
        matriz_supervizor.append(fila)

    convivencia = list(map(int, linea[inicio + 1 + num_empleados].strip().split()))
    return num_empleados, matriz_supervizor, convivencia

def set_independiente(seleccion_empleados, matriz_supervizor):
    for i in seleccion_empleados:
        for j in seleccion_empleados:
            if i != j and matriz_supervizor[i][j] == 1:
                return False
    return True

def calificaciones_total(seleccion_empleados, calificaciones):
    return sum(calificaciones[i] for i in seleccion_empleados)

def representacion_binaria(o, l):
    binario = bin(o)[2:].zfill(l)
    return [int(t) for t in binario]