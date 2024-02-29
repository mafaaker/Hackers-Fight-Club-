#Verano Peralta Maria Fernanda
#Tarea 3 
# Analisis de texto. 
#Recibe: lista de cadenas, puede contener espacios. 
#Regresa: Numero total de palabras en el texto. Numero total de caracteres (sin contar espacios en blanco). Numero de veces que aparece cada palabra. Encuentre la palabra más común en el texto. 

def text(cadenas):
    # Combinar todas las cadenas en una sola cadena
    comb = ' '.join(cadenas)
    # Dividir el texto en palabras
    palabras = comb.split()
    # Contar el número total de palabras
    total = len(palabras)
    # Calcular el número total de caracteres (sin contar espacios en blanco)
    caracteres = sum(len(palabra) for palabra in palabras)
    # Almacenar la frecuencia de cada palabra
    frecuencia_palabras = {}
    # Iterar sobre cada palabra en el texto y actualizar su frecuencia en el diccionario
    for palabra in palabras:
        frecuencia_palabras[palabra] = frecuencia_palabras.get(palabra, 0) + 1
    # Encontrar la palabra más común
    palabra_comun = max(frecuencia_palabras, key=frecuencia_palabras.get)
    # Devolver los resultados
    return total, caracteres, frecuencia_palabras, palabra_comun
# Ejemplo
cadenas = ["Este es un ejemplo de texto", "texto de ejemplo texto texto texto"]
resultado = text(cadenas)
total, caracteres, frecuencia_palabras, palabra_comun = resultado
print("Total de palabras:", total)
print("Total de caracteres:", caracteres)
print("Número de veces que aparece cada palabra:")
for palabra, frecuencia in frecuencia_palabras.items():
    print(f"- {palabra}: {frecuencia}")
print("Palabra común:", palabra_comun)
