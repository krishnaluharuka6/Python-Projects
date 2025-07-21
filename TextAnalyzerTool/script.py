"""Count total words, characters, unique words
Find most common word
Remove punctuation, stopwords (basic ones) 
Can extend with file handling later"""

import string
sentence = "Python is simple, powerful, and versatile. Python helps you think clearly."
sentence_clean = sentence.lower()
punctuation = string.punctuation
sentence_clean = "".join([char for char in sentence_clean if char not in punctuation])
print(f"Text after removing punctuation: {sentence_clean}")

words = sentence_clean.split()
total_words = len(words)
print(f"The total number of words are: {total_words}")

total_character = len(sentence_clean)
print(f"The total number of characters (no punctuation) are: {total_character}")

word_frequency = {}

for word in words:
    word_frequency[word] = word_frequency.get(word,0) + 1

unique_words = [key for key,value in word_frequency.items() if value == 1]
print(f"The unique words are {unique_words}")

max_freq = max(word_frequency.values())
common_words = {index for index,value in word_frequency.items() if value == max_freq}
print(f"The most common words are {common_words}")




stop_words = "is, am, are, the, in, on, of, you, and, but, to, a, an"
remove_stopword = [word for word in words if word not in stop_words]
print(f"text after removing stop words: {remove_stopword}")


