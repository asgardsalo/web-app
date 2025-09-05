#!/usr/bin/env python3

def suma(x, y):
    return x + y

def resta(x, y):
    return x - y

def multiplicación(x, y):
    return x * y

def división(x, y):
    if y == 0:
        raise ValueError("❌ No se puede dividir entre cero")
    return x / y

def potencia(x, y):
    return x ** y


def main():
    print("🔢 Calculadora Simple")
    print("===================")

    while True:
        print("\nSelecciona la operación:")
        print("1. Sumar (+)")
        print("2. Restar (-)")
        print("3. Multiplicar (*)")
        print("4. Dividir (/)")
        print("5. Potencia (x^y)")
        print("0. Salir")

        choice = input("Selecciona una opción: ")

        if choice == "0":
            print("👋 Saliendo de la calculadora. ¡Adiós!")
            break

        if choice not in {"1", "2", "3", "4", "5"}:
            print("⚠️ Opción inválida, por favor intenta de nuevo.")
            continue

        try:
            num1 = float(input("Ingrese primer número: "))
            num2 = float(input("Ingrese segundo número: "))
        except ValueError:
            print("⚠️ Caracter inválido, por favor ingrese solo números.")
            continue

        try:
            if choice == "1":
                print(f"✅ Resultado: {suma(num1, num2)}")
            elif choice == "2":
                print(f"✅ Resultado: {resta(num1, num2)}")
            elif choice == "3":
                print(f"✅ Resultado: {multiplicación(num1, num2)}")
            elif choice == "4":
                print(f"✅ Resultado: {división(num1, num2)}")
            elif choice == "5":
                print(f"✅ Resultado: {potencia(num1, num2)}")
        except Exception as e:
            print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()