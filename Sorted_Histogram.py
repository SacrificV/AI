filename = input("Enter file name: ")

try:
    with open(filename, "r") as f:
        text = f.read()

    freq = {}

    for ch in text:
        if ch.isalpha():
            ch = ch.lower()
            freq[ch] = freq.get(ch, 0) + 1

    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    out_file = filename + ".hist"

    with open(out_file, "w") as f:
        for ch, count in sorted_freq:
            f.write(f"{ch} -> {count}\n")

    print("Histogram saved to", out_file)

except FileNotFoundError:
    print("File not found")