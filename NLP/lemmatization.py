import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

words = stopwords.words('english')


nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

lemmatizer = WordNetLemmatizer()

sentence = input("Enter a sentence: ")

words = nltk.word_tokenize(sentence)

print("\nLemmatized Words (as nouns by default):")
for word in words:
    print(f"{word} → {lemmatizer.lemmatize(word)}")


print("\nLemmatizing as adjectives:")
for word in words:
    print(f"{word} → {lemmatizer.lemmatize(word, pos='a')}")