import random
import prompt

ROUNDS = 3
MIN_NUMBER = 1
MAX_NUMBER = 100


def is_even(n: int) -> bool:
    return n % 2 == 0


def play(player_name: str) -> None:

    print('Answer "yes" if the number is even, otherwise answer "no".')

    for _ in range(ROUNDS):
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        print(f"Question: {number}")

        answer = prompt.string("Your answer: ").strip().lower()
        correct_answer = "yes" if is_even(number) else "no"

        if answer != correct_answer:
            print(f"'{answer}' is wrong answer ;. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {player_name}!")
            return

        print("Correct!")

    print(f"Congratulations, {player_name}!")
