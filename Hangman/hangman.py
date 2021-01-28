# Hangman
def hangman(word):
    # The number of times the player guesses a wrong letter
    mistakes = 0
    stages = ["_________________________",
              "             |           ",
              "             |           ",
              "             0           ",
              "            /|\          ",
              "            / \          ",
              "You couldn't save the poor guy...", ]
    # Setting the board size as a variable with its size corresponding to the length of the given word
    # and making a list with each letter of the given word for the index to be accessed.
    board = ["_"] * len(word)
    remaining_letters = list(word.lower())
    print("Welcome To Hangman!")
    print(board)

    while True:
        guess = input("guess a letter from the word: ").lower()
        # what to do if the guess letter is right
        if guess in remaining_letters:
            ind = remaining_letters.index(guess)
            board[ind] = guess
            remaining_letters[ind] = "$"
            print(board)
        # if the guessed letter is wrong
        else:
            mistakes += 1
            print("\n".join(stages[0:mistakes]))

        # if all the letters are chosen correctly
        if "_" not in board:

            print("You won!\nYou saved him!")
            x = "".join(board)
            print(f"'{x}' is the right word!")
            print(""""
_________________________
         |          
        /
        
        Uwu  ....oO(Thank You so much for saving me...I owe you my life!)
        /|\         
 _______/_\________________        """)
            break
        # if the hangman dies
        if mistakes >= 7:
            print("You Lost! Well Played though :)")
            print(f"The right word was '{word}'")
            break


# a word needs to be used as a parameter of the 'hangman' function and that function needs to be called
# for the game to be playable :) | like the following line :)
# it could be a sentence too but that would make the game too hard to play :)
hangman("any word")
