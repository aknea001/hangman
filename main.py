# add api to get random word later
word = "testing"

def main(word):
    letterAmounts = ""

    for i in word:
        letterAmounts += "_ "

    print(f"{letterAmounts} \n")

if __name__ == "__main__":
    main(word)