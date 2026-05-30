import random

# List of predefined words
words = ["python", "laptop", "school", "friend", "garden"]

secret_word = random.choice(words)
guessed_letters = []

# Number of allowed wrong guesses
wrong_guesses = 0
max_wrong = 6

print("===== HANGMAN GAME =====")
print("Guess the word one letter at a time")

while wrong_guesses < max_wrong:
    display_word = ""

    # Show guessed letters and underscores
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Wrong guesses left:", max_wrong - wrong_guesses)

    # Check if word is completed
    if "_" not in display_word:
        print("Congratulations! You guessed the word:", secret_word)
        break


    guess = input("Enter a letter: ").lower()

    if len(guess) != 1:
        print("Please enter only one letter")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter")
        continue

    
    guessed_letters.append(guess)

   
    if guess in secret_word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

# When player is lost 
if wrong_guesses == max_wrong:
    print("\nGame Over! You lost")
    print("The word was:", secret_word)