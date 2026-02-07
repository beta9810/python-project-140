import random
import math

DESCRIPTION = (
    'Answer "yes" if given number is prime.'
    'Otherwise answer "no".'
)
MIN_NUMBER = 1
MAX_NUMBER = 100


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
   
    if n % 2 == 0:
        return False
    
    limit = int(math.isqrt(n))
    d = 3
    while d <= limit:
        if n % d == 0:
            return False
        d += 2
    return True


def generate_round():
    """
    Genera una ronda del juego '¿Número primo?'.
    Devuelve (question, correct_answer) como strings.
    """
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = str(number)
    correct_answer = "yes" if is_prime(number) else "no"
    return question, correct_answer
