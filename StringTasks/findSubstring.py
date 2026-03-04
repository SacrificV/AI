def find_all_substring_indexes(main_string, substring):
    indexes = []
    start_index = 0
    while True:
        index = main_string.find(substring, start_index)
        if index == -1:
            break
        indexes.append(index)
        start_index = index + 1
    return indexes
text = "abracadabra"
sub = "ab"
occurrences = find_all_substring_indexes(text, sub)
print(f"The substring '{sub}' appears at indexes: {occurrences}")