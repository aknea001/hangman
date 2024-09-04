# add api to get random word later
word = "testing"

def main(word):
    letterAmounts = ""
    letterNum = 0

    for i in word:
        letterAmounts += "_ "
        letterNum += 1

    print(f"{letterAmounts} \n\nThere are {letterNum} letters in the word..")

if __name__ == "__main__":
    main(word)