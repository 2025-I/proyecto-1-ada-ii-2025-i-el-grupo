#Fiesta de compañia
from .usar import set_independiente, calificaciones_total, representacion_binaria

def compañia_fuerza_bruta(num_empleados, supervisor_matriz, convivencia):
    maxima_calificacion = -1
    mejor_combinacion = None

    for indice_com in range(2**num_empleados):
        binario = representacion_binaria(indice_com, num_empleados)
        seleccion_empleados = [i for i, s in enumerate(binario) if s == 1]

        if set_independiente(seleccion_empleados, supervisor_matriz):
            total_calificacion = calificaciones_total(seleccion_empleados, convivencia)

            if total_calificacion > maxima_calificacion:
                maxima_calificacion = total_calificacion
                mejor_combinacion = binario
            
    return mejor_combinacion, maxima_calificacion
        
def main():
    # Ejemplo de prueba (copiado del PDF)
    num_empleados = 5
    supervisor_matriz = [
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0],
    ]
    convivencia = [10, 30, 15, 5, 8]

    resultado, calificacion = compañia_fuerza_bruta(num_empleados, supervisor_matriz, convivencia)

    print("Resultado:", resultado)
    print("Suma de calificaciones:", calificacion)