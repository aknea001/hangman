import requests

url = "https://random-word-api.herokuapp.com/word?lang=en"

response = requests.get(url)

if response.status_code == 200:

    word = response.json()[0]
else:
    print(f"Failed to retrieve word: {response.status_code}")


def main(word):
    letterAmounts = ""
    letterNum = 0
    letterList = []
    revealAnswer = []

    for i in word:
        letterAmounts += "_ "
        letterNum += 1
        letterList.append(i)
        revealAnswer.append("_")

    print(f"{letterAmounts} \n\nThere are {letterNum} letters in the word..")
    
    while True:
        if "_" not in revealAnswer:
            break

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
            for i in range(len(letterList)):
                if letterList[i] == guess:
                    revealAnswer[i] = guess
        
        #print(letterList)

        print(" ".join(revealAnswer))

    print("Good Job!")

if __name__ == "__main__":
    #main(word)
    print("")