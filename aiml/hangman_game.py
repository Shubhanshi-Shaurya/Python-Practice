import random
words = ["python", "computer", "algorithm", "artificial", "intelligence"]
word = random.choice(words)
guessed = []
attempts = 6
print("HANGMAN")
while attempts > 0:
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "
    print("\nWord:", display)
    print("Attempts left:", attempts)
    if all(letter in guessed for letter in word):
        print("You won!")
        break
    guess = input("Enter a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Enter a single letter.")
        continue
    if guess in guessed:
        print("You already guessed that letter.")
        continue
    guessed.append(guess)
    if guess in word:
        print("Correct guess!")
    else:
        print("Wrong guess!")
        attempts -= 1
if attempts == 0:
    print("\nYou lost!")
    print("The word was:", word)