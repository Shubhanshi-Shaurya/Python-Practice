import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

sentence = input("Enter a sentence: ")

lower_text=sentence.lower()

words = word_tokenize(lower_text)
words.sort()

print("\nWords in alphabetical order:")

for word in words:
    print(word)