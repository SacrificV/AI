def read_error(filename):
    with open(filename) as f:
        for line in f:
            if "ERROR" in line:
                print(line.strip())
read_error("ERR.txt")
