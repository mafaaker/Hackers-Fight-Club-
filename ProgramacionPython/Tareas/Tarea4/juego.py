#Verano Peralta María Fernanda
#Tarea 4
#Juego de adivina el número. 
#Escribe un script que genere un número aleatorio entre 1 y 100, sin utilizar ningún módulo de Python. Permita al usuario adivinar el número. El programa debe proporcionar retroalimentación al usuario (mayor, menor o correcto) después de cada intento. El juego debe continuar hasta que el usuario adivine el número o decida salir.
def numero_aleatorio():
    # Utilizamos una variable global numero para generar el número "aleatorio"
    global numero
    numero = (numero * 987654321 + 123456789) % 100
    return numero + 1  # Asegurar que el número esté entre 1 y 100
def adivina():
    global numero
    numero = 123456789  # numero inicial
    intentos = 0
    print("¡Bienvenidx!")
    print("Intenta adivinar el número secreto entre 1 y 100.")
    print("Escribe 'salir' para terminar el juego.")
    while True:
        intento = input("Ingresa tu intento: ")
        if intento.lower() == 'salir':
            print("¡Hasta luego!")
            break
        intento = int(intento)
        intentos += 1
        aleatorio = numero_aleatorio()
        #print({aleatorio}) #para asegurar que si esta generando números "aleatorios"
        if intento < aleatorio:
            print("El número secreto es mayor.")
        elif intento > aleatorio:
            print("El número secreto es menor.")
        else:
            print(f"¡Felicidades! ¡Has adivinado el número secreto ({aleatorio}) en {intentos} intentos!")
            break
# Iniciar el juego
adivina()
