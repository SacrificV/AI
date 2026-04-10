def read_logs(filename):
    with open(filename, "r") as f:
        for line in f:
            yield line.strip()
def parse_logs(lines):
    for line in lines:
        try:
            timestamp, level, message = map(str.strip, line.split("|", 2))
            date, time = timestamp.split()
            hour = time.split(":")[0]
            yield hour, level, message
        except ValueError:
            continue
def filter_logs(records):
    for hour, level, message in records:
        if level == ("ERROR", "WARNING"):
            yield hour,level
def count_logs(records):
    result = {}
    for hour, level in records:
        if hour not in result:
            result[hour] = {"ERROR" : 0, "WARNING" : 0}
        result[hour][level] += 1
    return result

def main():
    lines = read_logs("log.txt")
    parsed = parse_logs(lines)
    filtered = filter_logs(parsed)
    counts = count_logs(filtered)
    sorted_counts = sorted(
        counts.items(),
        key=lambda x: x[1]["ERROR"] + x[1]["WARNING"],
        reverse=True
    )
    for hour, data in sorted_counts:
        print(hour, data)
if __name__ == "__main__":
    main()