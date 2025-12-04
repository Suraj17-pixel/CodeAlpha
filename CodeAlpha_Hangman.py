import random

def hangman_game():
    # Predefined word list
    words = ["PYTHON", "PROGRAMMING", "COMPUTER", "KEYBOARD", "DEVELOPER"]
    
    # Select a random word
    secret_word = random.choice(words)
    guessed_word = ["_"] * len(secret_word)
    incorrect_guesses = 0
    max_incorrect = 6
    guessed_letters = []
    
    print("🎮 Welcome to Hangman!")
    print(f"The word has {len(secret_word)} letters.")
    print(" ".join(guessed_word))
    print(f"You have {max_incorrect} incorrect guesses allowed.\n")
    
    while incorrect_guesses < max_incorrect and "_" in guessed_word:
        # Get user input
        guess = input("Guess a letter: ").upper()
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue
            
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.\n")
            continue
            
        guessed_letters.append(guess)
        
        # Check if letter is in the word
        if guess in secret_word:
            print(f"Good guess! '{guess}' is in the word.\n")
            # Update the guessed word
            for i, letter in enumerate(secret_word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"Incorrect guesses: {incorrect_guesses}/{max_incorrect}\n")
        
        # Display current progress
        print("Word: ", " ".join(guessed_word))
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        print("-" * 40)
    
    # Game result
    if "_" not in guessed_word:
        print(f"🎉 Congratulations! You guessed the word: {secret_word}")
        print(f"Score: {max_incorrect - incorrect_guesses}/{max_incorrect} points")
    else:
        print(f"💀 Game Over! The word was: {secret_word}")
        print("Better luck next time!")

if __name__ == "__main__":
    hangman_game()
