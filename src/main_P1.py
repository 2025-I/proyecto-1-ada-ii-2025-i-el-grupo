import sys
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from Problema_1.Fuerza_bruta import subsecuencia_mas_larga_palindromo
from Problema_1.Ruta_dinamica import subsecuencia_larga_dinamica
from Problema_1.Ruta_voraz import subsecuencia_larga_voraz

def main():

    Tk().withdraw()
    filepath = askopenfilename(
        title="Selecciona el archivo de entrada (Problema 1)",
        filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
    )
    if not filepath:
        print("No se seleccionó archivo.", file=sys.stderr)
        sys.exit(1)
    with open(filepath, encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]
    try:
        n = int(lines[0])
    except (IndexError, ValueError):
        print("Error: la primera línea debe ser un entero (n).", file=sys.stderr)
        sys.exit(1)

    if len(lines) - 1 < n:
        print(f"Error: se esperaban {n} cadenas, pero solo hay {len(lines)-1}.", file=sys.stderr)
        sys.exit(1)

    solver = subsecuencia_larga_voraz          

    for i in range(1, n+1):
        cadena = lines[i]
        subseqs, _ = solver(cadena)
        print(" ".join(subseqs).lower())

if __name__ == "__main__":
    main()
