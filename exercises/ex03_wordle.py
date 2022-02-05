"""EX03 - A more structured edition of one shot wordle with a few new features!"""

__author__ = "730461954"


def contains_char(secret_word: str, letter: str) -> bool:
    """This function will search through the secret word, looking for the designated letter."""
    assert len(letter) == 1 
    i: int = 0 
    while i < len(secret_word):
        if letter == secret_word[i]:
            return True 
        i += 1
    return False 


def emojified(guess: str, secret_word: str) -> str: 
    """This fuction makes use of the contains_char function by calling it to test for yellow or white box codification."""
    assert len(guess) == len(secret_word)
    ind_guess: int = int(len(guess) - len(guess))
    emoji: str = str("")
    while ind_guess < len(secret_word):
        if guess[ind_guess] == secret_word[ind_guess]:
            emoji = emoji + str("\U0001F7E9")  # this is the block that runs when the character from the guess that is being checked matches the same character in the secret word
        in_word: bool = bool(False)
        ind_secret: int = int(len(secret_word) - len(secret_word))
        while contains_char(secret_word, guess[ind_guess]) and ind_secret < len(secret_word) and guess[ind_guess] != secret_word[ind_guess]:  # this while loop is checking for yellows 
            if guess[ind_guess] == secret_word[ind_secret]:
                in_word = True
            ind_secret = ind_secret + 1 
        if int(in_word) == 1:  # this if-else is checking to see if there should be a yellow or white printed for the given index
            emoji = emoji + str("\U0001F7E8")
        else:
            if guess[ind_guess] != secret_word[ind_guess]:
                emoji = emoji + str("\U00002B1C")
        ind_guess = ind_guess + 1

    return emoji


def input_guess(expected_length: int) -> str:
    """This function ensures that the input word is of the correct length."""
    word: str = input(f"Enter a {expected_length} character word: ") 
    while len(word) != expected_length:
        word = input(f"That wasn't {expected_length} chars! Try again: ")
    return word


def main() -> None:
    """The entrypoint of the program and the main game loop."""
    secret_word: str = str("codes")
    n_guesses: int = 1
    while n_guesses <= 6: 
        print(f"== Turn {n_guesses}/6 ==")
        word: str = input_guess(len(secret_word))
        print(emojified(word, secret_word))
        if word == secret_word:
            print(f"you won in {n_guesses}/6 turns!")
            return
        n_guesses += 1
    print("X/6 - Sorry, try again tomorrow!")   
    return


if __name__ == "__main__":
    main()
