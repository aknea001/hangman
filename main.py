# add api to get random word later
word = "testing"

def main(word):
    letterAmounts = ""
    letterNum = 0
    letterList = []

    for i in word:
        letterAmounts += "_ "
        letterNum += 1
        letterList.append(i)

    print(f"{letterAmounts} \n\nThere are {letterNum} letters in the word..")
    
    while True:
        while True:
            try:
                guess = input("Guess a letter..\n>> ")
                if guess.isalpha() and len(guess) == 1:
                    break
                else:
                    print("Please guess only an alphabetical letter\n\n")
            except Exception as e:
                print(f"ERROR getting letter: {e}")
        
        if guess in letterList:
            print("You got a letter yay")

if __name__ == "__main__":
    main(word)