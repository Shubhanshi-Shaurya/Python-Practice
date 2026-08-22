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


###
import random

# Words known by AI
words = [
    "apple", "angle", "animal", "arrow",
    "bread", "brain", "chair", "class",
    "dance", "dream", "earth", "engine",
    "flower", "friend", "garden", "happy",
    "house", "machine", "market", "mouse",
    "music", "orange", "paper", "phone",
    "plant", "python", "river", "school",
    "science", "student", "teacher", "tiger",
    "train", "water", "world"
]

word = random.choice(words)

used = []
wrong = 0


# AI finds possible words and chooses a letter
def ai_guess(pattern):

    possible = []

    # Find matching words
    for i in words:

        if len(i) != len(pattern):
            continue

        for j in range(len(pattern)):

            if pattern[j] != "_" and pattern[j] != i[j]:
                break

        else:
            possible.append(i)

    # Find the best letter
    best = ""
    best_count = 0

    for i in "abcdefghijklmnopqrstuvwxyz":

        if i in used:
            continue

        count = 0

        for j in possible:

            if i in j:
                count += 1

        if count > best_count:
            best_count = count
            best = i

    return best, possible


# Game
while wrong < 6:

    pattern = ""

    for i in word:

        if i in used:
            pattern += i
        else:
            pattern += "_"

    print("\nWord:", pattern)
    print("Used:", used)
    print("Wrong:", wrong)

    # Check win
    if "_" not in pattern:
        print("\nAI WON!")
        print("Word:", word)
        break

    # AI makes a guess
    guess, possible = ai_guess(pattern)

    print("Possible Words:", possible)
    print("AI Guess:", guess)

    used.append(guess)

    # Check guess
    if guess in word:
        print("Correct!")
    else:
        print("Wrong!")
        wrong += 1

# AI loses
if wrong == 6:
    print("\nAI LOST!")
    print("Word:", word)