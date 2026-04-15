import os
import shutil
from datetime import datetime
source = "project/data"
backup = os.path.join("backup", datetime.now().strftime("%Y-%m-%d"))
os.makedirs(backup, exist_ok=True)
for file in os.listdir(source):
    if file.endswith(".txt"):
        shutil.copy(os.path.join(source, file), os.path.join(backup, file))