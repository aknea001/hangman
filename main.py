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
            except Exception as e:
                print(f"ERROR getting letter: {e}")
        print("hi")
        break

if __name__ == "__main__":
    main(word)