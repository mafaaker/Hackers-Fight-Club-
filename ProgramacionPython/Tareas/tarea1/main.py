#Verano Peralta Maria Fernanda
#Tarea 1 
#Hacer una funcion que encuentre el palindromo más grande contenido en una cadena. Recibe: cadena a validar, regresa: cadena (palindromo más grande)
def palindromo(cadena):
 #Inicializando cadena
  pal = ""
  # Iterar sobre cada caracter en la cadena
  for i in range(len(cadena)):
      # Buscar palíndromos con centro en i (de longitud impar)
      izq, der = i, i
      while izq >= 0 and der < len(cadena) and cadena[izq] == cadena[der]:
          if der - izq + 1 > len(pal):
              pal = cadena[izq:der + 1]
          izq -= 1
          der += 1
      # Buscar palíndromos con centro entre i y i+1 (de longitud par)
      izq, der = i, i + 1
      while izq >= 0 and der < len(cadena) and cadena[izq] == cadena[der]:
          if der - izq + 1 > len(pal):
              pal = cadena[izq:der + 1]
          izq -= 1
          der += 1
  return pal
#Ejemplo
cadena = "ana rapar reconocer"
resultado = palindromo(cadena)
print("El palíndromo más grande en la cadena es:", resultado)
print("-----------------------------------------") 

#Hacer una funcion que determine si un numero es primo o no. Recibe: entero (número a validar), regresa: booleano. 
import math
def primo(numero):
    # Iterar sobre los números desde 2 hasta la raíz cuadrada de n
    for i in range(2, int(math.sqrt(numero)) + 1):
        # Si numero es divisible, no es primo
        if numero % i == 0:
            return False
    # Si no se encuentra ningún divisor, es primo
    return True
# Ejemplo
print(primo(17)) 
print(primo(5))
print(primo(24))   
print(primo(102)) 
print("-----------------------------------------") 

#Hacer una funcion RECURSIVA que agregue en una lista los primeros n números primos, regresa: lista. 
def n_primos(n, lista=None, num=2):
  if lista is None:
      lista = []
  if len(lista) == n:
      return lista
  if primo(num):
      lista.append(num)
  return n_primos(n, lista, num + 1) 
# Ejemplo de uso
n = 5
print("Los primeros", n, "números primos son:", n_primos(n))
