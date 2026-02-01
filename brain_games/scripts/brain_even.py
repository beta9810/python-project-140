from brain_games.cli import welcome_user
from brain_games.games.even import play


def main():
    name = welcome_user() 
    play(name)             


if __name__ == "__main__":
    main()
