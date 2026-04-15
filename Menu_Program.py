import os
import shutil
from datetime import datetime
while True:
    print("\n1. Show files")
    print("2. Create folder")
    print("3. Move file")
    print("4. Show current date")
    print("5. Exit")

    choice = input("Choose option: ")
    if choice == "1":
        print(os.listdir())
    elif choice == "2":
        name = input("Enter folder name: ")
        os.makedirs(name, exist_ok=True)
        print("Folder created")

    elif choice == "3":
        src = input("Enter source file: ")
        dst = input("Enter destination path: ")
        shutil.move(src, dst)
        print("File moved")

    elif choice == "4":
        print(datetime.now().strftime("%Y-%m-%d"))

    elif choice == "5":
        break

    else:
        print("Invalid option")