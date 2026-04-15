import os
from datetime import datetime
os.makedirs("logs", exist_ok=True)
log_file = os.path.join("logs", "log.txt")
with open(log_file, "a") as f:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    f.write(f"{now}- Program started\n")