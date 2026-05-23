import os
import sys
import functions as f


# region Casos


def make_iterative_permutation():
    """Pide al usuario un número y calcula su permutación usando factorial iterativo"""

    f.print_margin("Has elegido: Calcular permutaciones (factorial iterativo)")
    n = f.get_integer("| Ingrese el valor de n (entero no negativo)", 0)
    if n is None:
        return
    result: int = f.iterative_factorial(n)

    f.print_margin(f"Puedes permutar {n} elementos de {result} formas diferentes")
    f.print_margin("Calculado de forma iterativa")
    f.blank_line()


def make_recursive_permutation():
    """Pide al usuario un número y calcula su permutación usando factorial recursivo con
    optimización de cola (TCO)
    """

    f.print_margin("Has elegido: Calcular permutaciones (factorial recursivo)")
    n = f.get_integer("| Ingrese el valor de n (entero no negativo)", 0)
    if n is None:
        return

    result1: int = f.recursive_factorial(n)
    f.print_margin(f"Puedes permutar {n} elementos de {result1} formas diferentes")
    f.print_margin("Calculado de forma recursiva")
    f.blank_line()

    result2: int = f.recursive_factorial_tco(n)
    f.print_margin(f"Puedes permutar {n} elementos de {result2} formas diferentes")
    f.print_margin("Calculado de forma recursiva con TCO")
    f.blank_line()


def make_k_permutation():
    """Pide al usuario dos números y calcula su k-permutación"""

    f.print_margin("Has elegido: Calcular k-permutaciones")
    n = f.get_integer("| Ingrese el valor de n (entero no negativo)", 0)
    if n is None:
        return
    k = f.get_integer("| Ingrese el valor de k (para permutación, n >= k)", 0)
    if k is None:
        return
    result = f.k_permutation(n, k)

    f.print_margin(
        f"Puedes elegir {k} elementos de un conjunto de {n} de {result} formas"
    )
    f.blank_line()


# endregion


# region Auxiliares


def print_header():
    """Imprime el encabezado de la calculadora"""

    print("+--------------------------------------------------------+")
    f.print_margin("      Calculadora de factoriales y permutaciones       |")
    print("+--------------------------------------------------------+")
    f.print_margin("Elige una opción                                       |")
    f.print_margin("1. Calcular permutaciones (factorial iterativo)        |")
    f.print_margin("2. Calcular permutaciones (factorial recursivo)        |")
    f.print_margin("3. Calcular k-permutaciones                            |")
    f.print_margin("4. Salir                                               |")
    print("+--------------------------------------------------------+")


# endregion


# Le pide elegir al usuario una opción hasta que decida salir
while True:
    print_header()

    # Bucle principal
    try:
        value = f.get_integer("| Ingrese su opción", 1, 4)
        f.blank_line()
        if value is None:
            f.print_margin("Saliendo (entrada cancelada)")
            break
        match value:
            case 1:
                make_iterative_permutation()
            case 2:
                make_recursive_permutation()
            case 3:
                make_k_permutation()
            case 4:
                f.print_margin("Saliendo")
                break
    except ValueError as e:
        os.system("cls" if os.name == "nt" else "clear")
        f.blank_line()
        f.print_margin(
            f"Error: {e}. Por favor, asegúrese de ingresar números enteros válidos."
        )
    except Exception as e:
        os.system("cls" if os.name == "nt" else "clear")
        f.blank_line()
        f.print_margin(f"Ocurrió un error inesperado: {e}")
