def longestWord(text):
    words = text.split()
    if not words:
        return ""
    longest_word = max(words, key=len)
    return longest_word
input_string = "python is not a java-script"
print(longestWord(input_string))

