## Calcula el factorial de un entero dado usando iteración
def iterative_factorial(n: int) -> int:
    # Error de valor si es menor que cero
    if n < 0:
        raise ValueError("Valor no válido")

    fact: int = 1
    for i in range(n):
        fact *= i + 1

    return fact

    # También podríamos usar esta opción (mueve el import al inicio si quieres)
    # import functools as f
    # return f.reduce(lambda x, y: x * y, range(1, n + 1))


## Calcula el factorial de un entero dado usando recursión
def recursive_factorial(n: int) -> int:
    # Error de valor si es menor que cero
    if n < 0:
        raise ValueError("Valor no válido")

    # Caso base y recursivo (operador ternario)
    return n * recursive_factorial(n - 1) if n else 1


## Implementa la k-permutación de un conjunto de n elementos para elegir k elementos
def k_permutation(n: int, k: int) -> int:
    # Error si alguno es menor que cero o si k es menor que n
    if k < 0 or n < 0 or k < n:
        raise ValueError(f"Valores no válidos: {n}, {k}")

    # ? n+1 para abarcar n. range no es inclusivo al final
    result: int = 1
    for i in range(n - k + 1, n + 1):
        result *= i

    return result


## Recibe un número del usuario con validaciones y extremos opcionales
def get_integer(
    msg: str = "| Ingrese un número: ", min: int = None, max: int = None
) -> int:
    value: int
    first_attempt: bool = True

    while True:
        # Intenta pasar a entero
        try:
            i = input(f"{f'{msg}: ' if first_attempt else '| Intenta de nuevo: '}")

            # Entrada cancelada
            if not i:
                print("| Entrada cancelada")
                break

            value = int(i)

            # Valida los extremos si los tiene
            if min is not None and value < min:
                raise ValueError
            if max is not None and value > max:
                raise ValueError

            break
        except ValueError:
            print("| [Error] Entrada no válida")
            first_attempt = False

    return value
