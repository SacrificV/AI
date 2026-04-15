import os
for item in os.listdir():
    if os.path.isdir(item):
        print("[DIR]",item)
    else:
        print("[FILE]",item)