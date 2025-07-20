from getpass import getpass

# Input the secret word (hidden from the player)
choose_word = getpass("Enter any word to your liking, challenger: ")

# Set the number of lives (2 extra tries beyond the word's length)
lives = len(choose_word) + 2
guesses = []
found = False  # Flag to check if the word has been guessed

# Game loop
while not found:
    # Display current guessed letters and underscores
    for letter in choose_word:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("")  # Newline after the word display

    # Player makes a guess
    guess = input(f"Lives left {lives}, Next guess: ").lower()

    # Add guess to the list
    guesses.append(guess)

    # If guess is wrong, reduce life
    if guess not in choose_word.lower():
        lives -= 1
        if lives == 0:
            break

    # Check if all letters are guessed
    found = True
    for letter in choose_word:
        if letter.lower() not in guesses:
            found = False

# Final result
if found:
    print("GG 🎉 You guessed the word!")
else:
    print("😞 Game Over! Better luck next time.")
