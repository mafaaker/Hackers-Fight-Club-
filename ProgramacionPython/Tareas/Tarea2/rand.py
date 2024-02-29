#Verano Peralta María Fernanda
#Tarea 2
#Funcion RECURSIVA que genere contraseñas seguras. 
#Recibe: entero (cantidad de minusculas), entero (cantidad de mayusculas), entero (cantidad de digitos). Regresa: cadena (contraseña)
import random
def generarContra(minusculas, mayusculas, digitos, contrasena=""):
    #Todas las categorías de caracteres están completas
    if minusculas == 0 and mayusculas == 0 and digitos == 0:
        return contrasena
    # Generar un número aleatorio entre 0 y 2 para decidir qué tipo de carácter agregar
    tipo = random.randint(0, 2)
    # Generar caracteres según el tipo seleccionado y la cantidad restante
    if tipo == 0 and minusculas > 0:
        nueva = chr(random.randint(97, 122))  # Letras minúsculas en el rango ASCII
        return generarContra(minusculas - 1, mayusculas, digitos, contrasena + nueva)
    elif tipo == 1 and mayusculas > 0:
        nueva = chr(random.randint(65, 90))  # Letras mayúsculas en el rango ASCII
        return generarContra(minusculas, mayusculas - 1, digitos, contrasena + nueva)
    elif tipo == 2 and digitos > 0:
        nuevo = str(random.randint(0, 9))  # Dígitos del 0 al 9
        return generarContra(minusculas, mayusculas, digitos - 1, contrasena + nuevo)
    else:
        # Si no se puede agregar el tipo de carácter seleccionado, intentar nuevamente
        return generarContra(minusculas, mayusculas, digitos, contrasena)
# Ejemplo
min = 5
may = 5
dig = 9
contrasena = generarContra(min, may, dig)
print("Contraseña:", contrasena)
