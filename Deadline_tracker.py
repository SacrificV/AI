from  datetime import datetime
deadline = input("Enter the deadline (YYYY-MM-DD): ")
deadline_date = datetime.strptime(deadline, "%Y-%m-%d")
today = datetime.today()
diff = (deadline_date - today).days
if diff >= 0:
    print(f"{diff} days left")
else:
    print("Deadline ended")


