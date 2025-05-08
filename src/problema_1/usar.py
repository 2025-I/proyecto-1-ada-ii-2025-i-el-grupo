import unicodedata

def normalizar(cadena):
    cadena = cadena.lower()
    return ''.join(c for c in cadena if c.isalnum())

def normalizar_2(cadena):
    return ''.join(c for c in unicodedata.normalize('NFD', cadena.lower()) if c.isalpha())

def es_palindromo(cadena):
    return cadena == cadena[::-1]
