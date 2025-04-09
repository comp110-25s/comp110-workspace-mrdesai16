"""Wordle exercise!"""

__author__: str = "730652974"


def contains_char(search_string: str, char_to_find: str) -> bool:
    """Checking if character is present in string"""
    assert len(char_to_find) == 1, f"len('{char_to_find}') is not 1"
    idx = 0
    while idx < len(search_string):
        if search_string[idx] == char_to_find:
            return True
        idx += 1
    return False


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    assert len(guess) == len(secret), "Guess must be the same length as secret"
    emoji_result = ""
    idx = 0
    while idx < len(guess):
        if guess[idx] == secret[idx]:
            emoji_result += GREEN_BOX
        elif contains_char(secret, guess[idx]):
            emoji_result += YELLOW_BOX
        else:
            emoji_result += WHITE_BOX
        idx += 1
    return emoji_result


def input_guess(expected_length: int) -> str:
    guess = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    guess_number = 1
    max_guess_number = 6
    won = False
    while guess_number <= max_guess_number and not won:
        print(f"=== Turn {guess_number}/{max_guess_number} ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            won = True
            print(f"You won in {guess_number}/{max_guess_number} turns!")
        else:
            guess_number += 1
    if not won:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
