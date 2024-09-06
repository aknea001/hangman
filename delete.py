import string

alphabet = []
vowels = ["a", "e", "i", "o", "u", "y"]
consonants = []

for i in string.ascii_lowercase:
    alphabet.append(i)

alphabet.remove("i")

for i in vowels:
    if i not in alphabet:
        vowels.remove(i)

print(alphabet)
print(vowels)