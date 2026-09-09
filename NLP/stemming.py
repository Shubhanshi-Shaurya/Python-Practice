import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize



nltk.download('punkt')
nltk.download('punkt_tab')

port = PorterStemmer()

sample = input("Enter a sentence: ")

print("\nStemmed words:")
for word in word_tokenize(sample):
    print(f"{word} -> {port.stem(word)}")