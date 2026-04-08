def read_file(filename):
    with open(filename, "r") as f:
        for line in f:
            yield line
def filter_errors(lines):
    for line in lines:
        if "ERROR" in line:
            yield line
def to_upper(lines):
    for line in lines:
        yield line.upper()
def pipeline(filename):
    return to_upper(filter_errors(read_file(filename)))
for line in pipeline("ERR.txt"):
    print(line)