import random

def choose_word():
    # You can add more words to the list
    words = ["python", "hangman", "programming", "computer", "developer"]
    return random.choice(words)

def display_word(word, guessed_letters):
    # Display the word with guessed letters filled in
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    print("Welcome to Hangman!")
    secret_word = choose_word()
    guessed_letters = []
    attempts = 6  # Number of attempts allowed

    while attempts > 0:
        print("\nAttempts left:", attempts)
        current_display = display_word(secret_word, guessed_letters)
        print("Current Word:", current_display)

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            print("Incorrect guess!")
            attempts -= 1

        if "_" not in display_word(secret_word, guessed_letters):
            print("\nCongratulations! You guessed the word:", secret_word)
            break

    if attempts == 0:
        print("\nSorry, you ran out of attempts. The word was:", secret_word)

if __name__ == "__main__":
    hangman()
