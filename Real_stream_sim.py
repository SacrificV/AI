import time
import random

def log_stream():
    events = ["INFO", "ERROR", "WARNING", "DEBUG", "RERUN"]
    while True:
        event = random.choice(events)
        yield f"{event}: smthng happened"
        time.sleep(1)

for log in log_stream():
    print(log)