

import random
import hangman_words as word_new
import hangman_art as life
# import files for more interactivity

# Update the word list to use the 'word_list' from hangman_words.py
# initially started with  this line: word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_new.word_list)
word_length = len(chosen_word)

# added flag to track endgame
end_of_game = False
lives = 6
print(life.logo)
# added as amnby lives as amny stages pictures are to get count of ilfe a s well as art

# Import the logo from hangman_art.py and print it at the start of the game.

# Testing code
print(f'Pssst, the solution is {chosen_word}.')


# Create blanks as many letters as in guess
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # If the user has entered a letter they've already guessed, print the letter that they already added it.

    # Check guessed letter and get the postion to replace in display word
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:

            if guess in display:
                print(f"{guess} is already choosen.Chose another letter")
            else:
                # otherwise replace that guess letter in display
                display[position] = letter

    # Check if user is wrong. you cant putin above else otherwise loop will keep on running every time.
    if guess not in chosen_word:

        # If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        lives -= 1
        print(f"{guess} is not in word.{lives} lives left .")
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # Import the stages from hangman_art.py
    print(life.stages[lives])
