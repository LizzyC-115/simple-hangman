import random


word_file = "fruits.txt"
words = open(word_file).read().splitlines()


def checkGuesses(target, prevGuesses, blank):
    """
    Runs the main logic of the game. Allows the user to guess a singular letter
    and checks if that guess is in the target word. Will reject any guesses
    that are no valid and respond accordingly. Not case-sensitive.
    """
    userGuess = (input("Pick a letter: ")).lower()
    guesses = len(target) + 2

    while (guesses > 0 and blank != target):
        if userGuess in blank or userGuess in prevGuesses:  # Repeated guess
            print("Please enter a new guess")

        elif userGuess == "" or len(userGuess) > 1: # Invalid guess
            print("Please enter a valid guess")

        elif userGuess not in target:   # Incorrect guess
            print(f"Letter {userGuess} is not in the target word")
            guesses -= 1
    
        else:   # Valid and correct guess
            index = target.find(userGuess)
            while (index != -1):
                blank = blank[:index] + userGuess + blank[index + 1:]
                index = target.find(userGuess, index + 1)
            print(blank)

        if (blank == target):
            print("YOU WON!!")
            return 0
    
        prevGuesses += userGuess
        userGuess = input("Pick a letter: ")
    
    return -1


def startGame():
    """
    Begins the game by randomly choosing a fruit from the fruits file
    and telling the player how many letters are in their target word,
    along with how many guesses they have.
    """
    target = (random.choice(words)).lower()

    print(f"Your word is a FRUIT of length {len(target)}. You have {len(target) + 2} guesses.")
    blank = ""
    for i in range(len(target)):
        blank += '_'
    prevGuesses = ""

    if checkGuesses(target, prevGuesses, blank) == -1:
        print(f"You lost. The target word was {target}")


def main():
    userInput = input("Type 'start' to begin or hit enter to quit ")
    while (userInput != ''):
        if (userInput.lower() == 'start'):
            startGame()
        else:
            print("Invalid input. ")
        userInput = input("Type 'start' to begin or hit enter to quit ")


if __name__=="__main__":
    main()