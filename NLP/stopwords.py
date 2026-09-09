import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt_tab')
nltk.download('stopwords')

text = input("Enter a sentence: ")

words = word_tokenize(text)


stop_words = set(stopwords.words('english'))
punctuations = set(string.punctuation)

found_stopwords = [word for word in words if word.lower() in stop_words]
found_punctuation = [word for word in words if word in punctuations]

filtered_words = [word for word in words if word.lower() not in stop_words and word not in punctuations]

print("Original words:", words)
print("Stopwords found:", found_stopwords)
print("Punctuation found:", found_punctuation)
print("Filtered words:", filtered_words)