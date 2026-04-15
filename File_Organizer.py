import os
import shutil

base = "downloads"
images = os.path.join(base, "images")
docs = os.path.join(base, "documents")

os.makedirs(images, exist_ok=True)
os.makedirs(docs, exist_ok=True)

for file in os.listdir(base):
    path = os.path.join(base, file)

    if os.path.isfile(path):
        if file.endswith((".png", ".jpg")):
            shutil.move(path, os.path.join(images, file))
        elif file.endswith((".txt", ".pdf")):
            shutil.move(path, os.path.join(docs, file))