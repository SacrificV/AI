filename = input("Enter filename: ")
try:
    with open(filename, "r") as f:
        text= f.read()

    freq = {}
    for ch in text:
        if ch.isalpha():
            ch = ch.lower()
            freq[ch] = freq.get(ch, 0) + 1

        for ch in sorted(freq.keys()):
            print(f"{ch} -> {freq[ch]}")
except FileNotFoundError:
    print("File not found")

