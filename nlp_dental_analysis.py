import nltk
from nltk.tokenize import word_tokenize
from collections import Counter

text = "The patient complains of tooth pain and gum bleeding"

tokens = word_tokenize(text)

word_count = Counter(tokens)

print("Word frequency:", word_count)