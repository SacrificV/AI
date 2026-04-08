def read_age_above_30(filename):
    with open(filename, "r") as f:
        header = next(f)
        for line in f:
            name, age = line.strip().split(",")
            if int(age) > 30:
                yield name, int(age)

for file in read_age_above_30("lyudi.csv"):
    print(file)

