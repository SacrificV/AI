class FileEmptyError(Exception):
    pass
class BadLineError(Exception):
    pass
filename = input("Enter file name: ")
try:
    with open(filename) as f:
        lines = f.readlines()
    if not lines:
        raise FileEmptyError("File is empty!")
    students = {}
    for line in lines:
        parts = line.strip().split()
        if len(parts) != 3:
            raise BadLineError("Bad line format")
        first, last, points = parts
        try:
            points = float(points)
        except ValueError:
            raise BadLineError("Invalid points value")

        key = (first, last)
        students[key] = students.get(key, 0) + points

    sorted_students = sorted(students.items(), key=lambda x: (x[0][1], x[0][0]))

    for (first, last), total in sorted_students:
        print(f"{first} {last} {total}")

except FileNotFoundError:
    print("File not found")
except FileEmptyError as e:
    print(e)
except BadLineError as e:
    print(e)