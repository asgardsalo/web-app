#!/usr/bin/env python3
"""
Simple Calculator Demo
Works on macOS and Windows
Author: Demo Engineer
"""

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("❌ Cannot divide by zero")
    return x / y

def power(x, y):
    return x ** y


def main():
    print("🔢 Simple Calculator")
    print("===================")

    while True:
        print("\nSelect operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Power (x^y)")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "0":
            print("👋 Exiting calculator. Goodbye!")
            break

        if choice not in {"1", "2", "3", "4", "5"}:
            print("⚠️ Invalid choice, please try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("⚠️ Invalid input, please enter numbers.")
            continue

        try:
            if choice == "1":
                print(f"✅ Result: {add(num1, num2)}")
            elif choice == "2":
                print(f"✅ Result: {subtract(num1, num2)}")
            elif choice == "3":
                print(f"✅ Result: {multiply(num1, num2)}")
            elif choice == "4":
                print(f"✅ Result: {divide(num1, num2)}")
            elif choice == "5":
                print(f"✅ Result: {power(num1, num2)}")
        except Exception as e:
            print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()