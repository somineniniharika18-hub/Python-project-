import random

words = ["python", "apple", "laptop", "school", "gaming"]

word = random.choice(words)

guessed_letters = []
incorrect_guesses = 0
max_guesses = 6

print("Welcome to Hangman Game!")

while incorrect_guesses < max_guesses:

    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    if "_" not in display_word:
        print("Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")

    elif guess in word:
        print("Correct guess!")
        guessed_letters.append(guess)

    else:
        print("Wrong guess!")
        guessed_letters.append(guess)
        incorrect_guesses += 1
        print("Remaining chances:", max_guesses - incorrect_guesses)

if incorrect_guesses == max_guesses:
    print("\nGame Over! The word was:", word)