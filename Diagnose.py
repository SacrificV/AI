def process(filename):
    with open(filename) as f:
#       data = f.readlines()
#        errors = [line for line in data if "ERROR" in line]
#        return [line.upper() for line in errors]
#       this is bad because we load entire file into memory which is bad if file is LARGE
        for line in f:
            if "ERROR" in line:
                yield line.upper()
# this 3 lines is better because we load file line by line and its single pass through the file