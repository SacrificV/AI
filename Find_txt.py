import os
for file in os.listdir():
    if file.endswith(".txt"):
        size = os.path.getsize( file) // 1024
        print(f"{file}-{size} KB")