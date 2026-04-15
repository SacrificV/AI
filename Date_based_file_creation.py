from datetime import datetime
now= datetime.now()
filename = now.strftime("%Y-%m-%d.txt")
with open(filename, "w") as f:
    f.write(now.strftime("%H:%M:%S"))