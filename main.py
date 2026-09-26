from calculadora import sumar, restar, multiplicar, dividir


def main():
    print("=== CALCULADORA ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    opcion = input("Selecciona una opción: ")

    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))

    if opcion == "1":
        resultado = sumar(a, b)
    elif opcion == "2":
        resultado = restar(a, b)
    elif opcion == "3":
        resultado = multiplicar(a, b)
    elif opcion == "4":
        try:
            resultado = dividir(a, b)
        except ValueError as error:
            print(f"Error: {error}")
            return
    else:
        print("Opción no válida")
        return

    print(f"Resultado: {resultado}")


if __name__ == "__main__":
    main()