"""EX02 - One Shot Wordle!"""

__author__ = "730461954"

secret_word: str = str("python")
count: str = str(len(secret_word))
guess: str = input(f"What is your {count}-letter guess? ")
# this block of code has established a few initial variables

while len(guess) != len(secret_word):
    guess = input(f"That was not {count} letters! Try again: ")
# this block of code has ensured that the guess has the correct amount of characters

ind_guess: int = int(len(guess) - len(guess))
emoji: str = str("")

while ind_guess < len(secret_word):
    if guess[ind_guess] == secret_word[ind_guess]:
        emoji = emoji + str("\U0001F7E9")  # this is the block that runs when the character from the guess that is being checked matches the same character in the secret word
    in_word: bool = bool(False)
    ind_secret: int = int(len(secret_word) - len(secret_word))
    while int(in_word) == 0 and ind_secret < len(secret_word) and guess[ind_guess] != secret_word[ind_guess]:  # this while loop is checking for yellows 
        if guess[ind_guess] == secret_word[ind_secret]:
            in_word = True
        ind_secret = ind_secret + 1 
    if int(in_word) == 1:  # this if-else is checking to see if there should be a yellow or white printed for the given index
        emoji = emoji + str("\U0001F7E8")
    else:
        if guess[ind_guess] != secret_word[ind_guess]:
            emoji = emoji + str("\U00002B1C")
    ind_guess = ind_guess + 1

print(emoji)

if guess == secret_word:  # this is the end of the program where the user is told if they were correct or not
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")