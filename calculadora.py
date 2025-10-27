import division,multiplicacion,resta,suma

def calculadora():
    print("=== Calculadora básica ===")
    while True:
        print("\nOperaciones disponibles:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        opcion = input("Elige una opción (1-5): ")

        if opcion == "5":
            print("¡Hasta luego!")
            break

        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))

        if opcion == "1":
            print("Resultado:", suma.suma(a, b))
        elif opcion == "2":
            print("Resultado:", resta.resta(a, b))
        elif opcion == "3":
            print("Resultado:", multiplicacion.multiplicar(a, b))
        elif opcion == "4":
            print("Resultado:", division.division(a, b))
        else:
            print("Opción no válida.")

calculadora()
