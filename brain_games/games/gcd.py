import random
import math

DESCRIPTION = "Find the greatest common divisor of given numbers."
MIN_NUMBER = 1
MAX_NUMBER = 100


def generate_round():
    """
    Genera una ronda del juego MCD.
    Devuelve (question, correct_answer) como strings.

    question: "a b"  (dos números separados por espacio)
    correct_answer: str(math.gcd(a, b))
    """
    a = random.randint(MIN_NUMBER, MAX_NUMBER)
    b = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = f"{a} {b}"
    correct_answer = str(math.gcd(a, b))
    return question, correct_answer
