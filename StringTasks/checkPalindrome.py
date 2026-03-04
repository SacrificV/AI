def check_palindrome(input_string):
    if input_string.lower() == input_string.lower()[::-1]:
        return True
    else:
        return False

input_string = "Bruh"
print(check_palindrome(input_string))