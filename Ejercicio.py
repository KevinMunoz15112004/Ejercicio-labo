import math

def calculo_seno(x, a=10):
    contador = 0
    for i in range(a):
        termino = ((-1)**i) * (x**(2*i+1)) / math.factorial(2*i+1)
        contador += termino
    return contador

def menu():
    while True:
        print("\nMenú de opciones:")
        print("1. Calcular seno")
        print("2. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            x = float(input("Ingresa el ángulo en grados: "))
            radian = math.radians(x)
            resultado = calculo_seno(radian)
            print(f"Seno de {x}° = {resultado:.3f}")
        elif opcion == "2":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

menu()
