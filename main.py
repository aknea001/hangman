import requests
import string
import re

url = "https://random-word-api.herokuapp.com/word?lang=en"

response = requests.get(url)

if response.status_code == 200:

    word = response.json()[0]
    
else:
    print(f"Failed to retrieve word: {response.status_code}")

#word = "test"

letterAmounts = ""
letterNum = 0
mistakes = 0
lives = 6
letterList = []
revealAnswer = []
guessing = False
usedLetters = []
alphabet = []

for i in string.ascii_lowercase:
    alphabet.append(i)


def getGuess():
    global guessing
    global mistakes

    while True:
        guess = input("Guess a letter..\n>> ").lower()
        if guess[0] == "!":
            commands(guess)
        elif bool(re.match("^[A-Za-z]+$", guess)) and len(guess) == 1:
            if guess in usedLetters:
                print("You've already tried this letter..")
            else:
                usedLetters.append(guess)
                alphabet.remove(guess)
                guessHandling(guess)
        else:
            print("Please guess only an alphabetical letter\n\n")

def guessHandling(guess):
    global mistakes

    if guess in letterList:
        for i in range(len(letterList)):
            if letterList[i] == guess:
                revealAnswer[i] = guess
    else:
        mistakes += 1
            
    endHandling()
    
    # print(letterList)

    print(open(f"hangmanPics/hangman{mistakes}.txt", "r").read())
    print(" ".join(revealAnswer))

def endHandling():
    if "_" not in revealAnswer:
        print(open(f"hangmanPics/hangman0.txt", "r").read())

        print(' '.join(letterList))
        print("Good Job! You did it!")

        exit()
    elif mistakes >= lives:
        print(open("hangmanPics/dead.txt", "r").read())
        print("You died :(\n x_x\n")
        print(f"The word was: {' '.join(letterList)}")

        exit()
    else:
        return
    
def commands(guess):
    global mistakes

    if guess[:2] == "!h" or guess[:6] == "!!help":
        print(open("help.txt", "r").read())
    elif guess[:2] == "!g" or guess[:7] == "!!guess":
        guess = guess.split()
        if len(guess) < 2:
            print(f"ERROR {guess[0]} only takes one argument..\nSyntax {guess[0]} your guess")
        elif guess[1] == word:
            print(open(f"hangmanPics/hangman0.txt", "r").read())
            print("Good Job! You did it!")

            exit()
        else:
            mistakes += 1

            print(open(f"hangmanPics/hangman{mistakes}.txt", "r").read())
            print(" ".join(revealAnswer))
            endHandling()
    elif guess[:2] == "!l" or guess[:9] == "!!letters":
        guess = guess.split()

        if len(guess) > 1:
            if guess[1] == "-t" or False:
                print(", ".join(usedLetters))
            elif guess[1] == "-r" or False:
                print(", ".join(usedLetters[::-1]))
            else:
                print(", ".join(sorted(usedLetters)))
        else:
            # print("no args")
            print(", ".join(sorted(usedLetters)))
    elif guess[:2] == "!a" or guess[:11] == "!!avaliable":
        print(", ".join(alphabet))


def main(word):
    global letterAmounts
    global letterNum
    
    for i in word:
        letterAmounts += "_ "
        letterNum += 1
        letterList.append(i)
        revealAnswer.append("_")

    print(open("hangmanPics/hangman0.txt", "r").read())
    print(f"{letterAmounts} \n\nThere are {letterNum} letters in the word..")

    print("PS: you can use !h to see different commands")

    getGuess()

if __name__ == "__main__":
    main(word)