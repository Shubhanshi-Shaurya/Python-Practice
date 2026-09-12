import nltk
import random
from nltk.corpus import movie_reviews

nltk.download('movie_reviews')

documents = [(list(movie_reviews.words(fileid)), category)
for category in movie_reviews.categories()
for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

print("\nSample Document (Words and Category):\n")
print(documents[1])

all_words = [w.lower() for w in movie_reviews.words()]
all_words = nltk.FreqDist(all_words)

print("\nMost Common Words:\n")
print(all_words.most_common(15))

print("\nFrequency of 'movie':", all_words["movie"])