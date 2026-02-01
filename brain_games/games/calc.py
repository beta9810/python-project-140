import operator
import random

DESCRIPTION = "What is the result of the expression?"

OPS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
}

MIN_NUMBER = 0
MAX_NUMBER = 20


def generate_round():
    a = random.randint(MIN_NUMBER, MAX_NUMBER)
    b = random.randint(MIN_NUMBER, MAX_NUMBER)
    op_symbol = random.choice(list(OPS.keys()))
    op_func = OPS[op_symbol]

    result = op_func(a, b)

    question = f"{a} {op_symbol} {b}"
    correct_answer = str(result)
    return question, correct_answer
