import string

text = "Bruh is BRuh and Bruh"
d = dict()
def count_words_frequency(text):
    text = text.lower()
    words = text.split(" ")
    for word in words:
        if word not in d:
            d[word] = 0
        if word in d:
            d[word] += 1
    return d
print(count_words_frequency(text))