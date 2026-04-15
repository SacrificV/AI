from datetime import datetime
now = datetime.now()
print("Year: ", now.year)
print("Weekday: ", now.strftime("%A"))