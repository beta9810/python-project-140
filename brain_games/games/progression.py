import random

DESCRIPTION = "What number is missing in the progression?"

MIN_LEN = 5
MAX_LEN = 10

START_MIN = 1
START_MAX = 20
STEP_MIN = 1
STEP_MAX = 10


def build_progression(start: int, step: int, length: int) -> list[int]:
    """Construye una progresión aritmética."""
    return [start + i * step for i in range(length)]


def generate_round():
    """
    Genera una ronda de 'Progresión Aritmética'.
    Devuelve:
      - question: str (progresión con '..' en la posición oculta)
      - correct_answer: str (el número oculto)
    """
    length = random.randint(MIN_LEN, MAX_LEN)
    start = random.randint(START_MIN, START_MAX)
    step = random.randint(STEP_MIN, STEP_MAX)

    progression = build_progression(start, step, length)

    # Elegir aleatoriamente la posición a ocultar
    hidden_index = random.randrange(length)
    correct_answer = str(progression[hidden_index])

    # Construir la pregunta con '..' en la posición oculta
    display = progression[:]
    display[hidden_index] = ".."
    question = " ".join(str(x) for x in display)

    return question, correct_answer
