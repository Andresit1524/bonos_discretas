"""funcions contiene todas las funciones para el desarrollo del Bono 1. Incluye algoritmos y
funciones auxiliares para la entrada y salide de datos.

Los algoritmos incluyen verificaiones de tipo, porque resulta que las anotaciones de tipo en Python
son de adorno literalmente >:(
"""

from typing import Optional


# region Algoritmos


def iterative_factorial(n: int) -> int:
    """Calcula el factorial de un entero dado usando iteración"""

    # Error si el valor no es entero
    if type(n) is not int:
        raise TypeError(f"Valor no válido: {n}")

    # Error de valor si es menor que cero
    if n < 0:
        raise ValueError(f"Valor no válido: {n}")

    fact: int = 1
    for i in range(n):
        fact *= i + 1

    return fact

    # También podríamos usar esta opción (mueve el import al inicio si quieres)
    # import functools as f
    # return f.reduce(lambda x, y: x * y, range(1, n + 1))


def recursive_factorial(n: int) -> int:
    """Calcula el factorial de un entero dado usando recursión"""

    # Error si el valor no es enterio
    if type(n) is not int:
        raise TypeError(f"Valor no válido: {n}")

    # Error de valor si es menor que cero
    if n < 0:
        raise ValueError(f"Valor no válido: {n}")

    # Caso base y recursivo (operador ternario)
    return n * recursive_factorial(n - 1) if n else 1


def recursive_factorial_tco(n: int, acum: int = 1) -> int:
    """Implementa el factorial de un número dado usando recursión y TCO"""

    # Error de tipo si el valor no es entero
    if type(n) is not int:
        raise TypeError(f"Valor no válido: {n}")

    # Error de valor si es menor que cero
    if n < 0:
        raise ValueError(f"Valor no válido: {n}")

    # Caso base
    if n == 0:
        return acum

    # Optimización de cola
    return recursive_factorial_tco(n - 1, acum * n)


def k_permutation(n: int, k: int) -> int:
    """Implementa la k-permutación de un conjunto de n elementos para elegir k elementos"""

    # Error de tipo si los valores no son enteros
    if type(n) is not int or type(k) is not int:
        raise TypeError(f"Valores no válidos: {n}, {k}")

    # Error si alguno es menor que cero o si n es menor que k
    if k < 0 or n < 0 or n < k:
        raise ValueError(f"Valores no válidos: {n}, {k}")

    result: int = 1
    for i in range(n - k + 1, n + 1):
        result *= i

    return result


# endregion


# region Entrada y salida


def get_integer(
    msg: str = "| Ingrese un número: ", min: int = None, max: int = None
) -> Optional[int]:
    """Recibe un número del usuario con validaciones y extremos opcionales"""

    value: int
    first_attempt: bool = True

    while True:
        # Intenta pasar a entero
        try:
            i = input(f"{f'{msg}: ' if first_attempt else '| Intenta de nuevo: '}")

            # Entrada cancelada
            if not i:
                print_margin("Entrada cancelada")
                return None

            value = int(i)

            # Valida los extremos si los tiene
            if min is not None and value < min:
                raise ValueError
            if max is not None and value > max:
                raise ValueError

            break
        except ValueError:
            print_margin("[Error] Entrada no válida")
            first_attempt = False

    return value


def blank_line():
    """Imprime una línea en blanco con amrgen"""
    print("| ")


def print_margin(text: str):
    """Imprime con un margen"""
    print(f"| {text}")


# endregion
