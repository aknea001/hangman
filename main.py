import requests

url = "https://random-word-api.herokuapp.com/word?lang=en"

response = requests.get(url)

if response.status_code == 200:

    word = response.json()[0]
    
else:
    print(f"Failed to retrieve word: {response.status_code}")

word = "test"

letterAmounts = ""
letterNum = 0
mistakes = 0
lives = 6
letterList = []
revealAnswer = []
guessing = False


def getGuess():
    global guessing
    global mistakes

    while True:
        try:
            if guessing:
                guessing = False

                guess = input("Which word do u want to guess?\n>> ")
                if guess == word:
                    print(open(f"hangmanPics/hangman0.txt", "r").read())
                    print("Good Job! You did it!")

                    exit()
                else:
                    mistakes += 1

                    print(open(f"hangmanPics/hangman{mistakes}.txt", "r").read())
                    print(" ".join(revealAnswer))
                    endHandling()
            else:
                guess = input("Guess a letter..\n>> ")
                if guess[0] == "-":
                    if guess == "-g" or guess == "--guess":
                        guessing = True
                elif guess.isalpha() and len(guess) == 1:
                    guessHandling(guess)
                else:
                    print("Please guess only an alphabetical letter\n\n")
        except Exception as e:
            print(f"ERROR getting letter: {e}")

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
        print("Good Job! You did it!")

        exit()
    elif mistakes >= lives:
        print(open("hangmanPics/dead.txt", "r").read())
        print("You died :(\n x_x\n")
        print(f"The word was: {' '.join(letterList)}")

        exit()
    else:
        return

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

    getGuess()

if __name__ == "__main__":
    main(word)