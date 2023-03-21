## Este código cuenta cuantas veces de repite el algoritmo: si tomamos un número n mayor que cero si es par lo dividimos entre 2 y si es impar lo multiplicamos por 3 y le sumamos 1
#eventualmente llegaremos al 1.

def steps_to_one(n):
    """
    Given a number n, count the number of steps it takes to reach 1
    using the following algorithm:
    - If n is even, divide it by 2
    - If n is odd, multiply it by 3 and add 1
    """
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
        steps += 1
    return steps