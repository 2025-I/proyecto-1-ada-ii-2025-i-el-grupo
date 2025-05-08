import sys
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from Problema_2.RFuerza_bruta import compañia_fuerza_bruta
from Problema_2.Ruta_dinamica import fiesta_dinamica
from Problema_2.Ruta_voraz    import fiesta_voraz

def main():
    Tk().withdraw()
    filepath = askopenfilename(
        title="Selecciona el archivo de entrada (Problema 2)",
        filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
    )
    if not filepath:
        print("No se seleccionó archivo.", file=sys.stderr)
        sys.exit(1)

    
    with open(filepath, encoding="utf-8") as f:
        lines = [l.strip() for l in f if l.strip()]
    try:
        p = int(lines[0])
    except (IndexError, ValueError):
        print("Error: la primera línea debe ser un entero (número de casos).", file=sys.stderr)
        sys.exit(1)
    idx = 1
    
    for _ in range(p):
        if idx >= len(lines):
            print("Error: faltan datos para el caso", file=sys.stderr)
            sys.exit(1)
        try:
            m = int(lines[idx])
        except ValueError:
            print(f"Error: línea {idx+1} no es un entero (m).", file=sys.stderr)
            sys.exit(1)
        idx += 1
        adj = []

        for i in range(m):
            if idx >= len(lines):
                print("Error: faltan filas de matriz de supervisión.", file=sys.stderr)
                sys.exit(1)
            row = list(map(int, lines[idx].split()))
            if len(row) != m:
                print(f"Error: la fila {i+1} de supervisión debe tener {m} columnas.", file=sys.stderr)
                sys.exit(1)
            adj.append(row)
            idx += 1
        if idx >= len(lines):
            print("Error: faltan las calificaciones.", file=sys.stderr)
            sys.exit(1)
        ratings = list(map(int, lines[idx].split()))
        if len(ratings) != m:
            print(f"Error: la línea de calificaciones debe tener {m} números.", file=sys.stderr)
            sys.exit(1)
        idx += 1
        invited, total = fiesta_voraz(m, adj, ratings)
        print(" ".join(str(bit) for bit in invited) + " " + str(total))

if __name__ == "__main__":
    main()
