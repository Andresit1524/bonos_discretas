import os
import bono_1.functions as f


# region Casos


def make_iterative_permutation():
    """Pide al usuario un número y calcula su permutación usando factorial iterativo"""

    print("| Has elegido: Calcular permutaciones (factorial iterativo)")
    n: int = f.get_integer("| Ingrese el valor de n (entero no negativo)", 0)
    result = f.iterative_factorial(n)

    print(f"| Puedes permutar {n} elementos de {result} formas diferentes")
    print("| Calculado de forma iterativa")
    print("| ")


def make_recursive_permutation():
    """Pide al usuario un número y calcula su permutación usando factorial recursivo"""

    print("| Has elegido: Calcular permutaciones (factorial recursivo)")
    n: int = f.get_integer("| Ingrese el valor de n (entero no negativo)", 0)
    result = f.recursive_factorial(n)

    print(f"| Puedes permutar {n} elementos de {result} formas diferentes")
    print("| Calculado de forma recursiva")
    print("| ")


def make_k_permutation():
    """Pide al usuario dos números y calcula su k-permutación"""

    print("| Has elegido: Calcular k-permutaciones")
    n: int = f.get_integer("| Ingrese el valor de n (entero no negativo)")
    k: int = f.get_integer("| Ingrese el valor de k (para permutación, n >= k)")
    result = f.k_permutation(n, k)

    print(f"| Puedes elegir {k} elementos de un conjunto de {n} de {result} formas")
    print("| ")


# endregion


# region Auxiliares


def print_header():
    """Imprime el encabezado de la calculadora"""

    print("+--------------------------------------------------------+")
    print("|       Calculadora de factoriales y permutaciones       |")
    print("+--------------------------------------------------------+")
    print("| Elige una opción                                       |")
    print("| 1. Calcular permutaciones (factorial iterativo)        |")
    print("| 2. Calcular permutaciones (factorial recursivo)        |")
    print("| 3. Calcular k-permutaciones                            |")
    print("| 4. Salir                                               |")
    print("+--------------------------------------------------------+")


# endregion


# Le pide elegir al usuario una opción hasta que decida salir
while True:
    print_header()

    # Bucle principal
    try:
        value: int = f.get_integer("| Ingrese su opción", 1, 4)
        print("| ")
        match value:
            case 1:
                make_iterative_permutation()
            case 2:
                make_recursive_permutation()
            case 3:
                make_k_permutation()
            case 4:
                print("| Saliendo")
                exit(0)
    except ValueError as e:
        os.system("cls" if os.name == "nt" else "clear")
        print(
            f"|\n| Error: {e}. Por favor, asegúrese de ingresar números enteros válidos."
        )
    except Exception as e:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"|\n| Ocurrió un error inesperado: {e}")
