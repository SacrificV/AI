def count_vowels(s):

    vowel_count = 0
    vowels = "aeiouAEIOU"
    for char in s:
        if char in vowels:
            vowel_count += 1
    return vowel_count


input_string = "aeiouAibruh"
count_1 = count_vowels(input_string)
print(f"The number of vowels in '{input_string}' is: {count_1}")


