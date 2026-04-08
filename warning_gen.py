def warning_lines(filename):
    with open(filename) as f:
        for line in f:
            if "WARNING" in line:
                yield line.strip()
for line in warning_lines("ERR.txt"):
    print(line)
