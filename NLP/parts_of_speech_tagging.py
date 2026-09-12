import nltk

from nltk.corpus import stopwords

words = stopwords.words('english')

#nltk.data.path.append(r"C:\Users\Shaurya Agarwal\AppData\Roaming\nltk_data")

nltk.download('punkt')

nltk.download('averaged_perceptron_tagger_eng')

nltk.download('punkt_tab')

text1 = input("Enter a paragraph of text: ")

print("\nOriginal Text:")

print(text1)

words1 = nltk.word_tokenize(text1)

print("\nTokenized Words:")

print(words1)

print("\nWords with POS Tags:")

print(nltk.pos_tag(words1))