import calendar
year = int(input("Enter year: "))
month = int(input("Enter month: "))
filename = f"{calendar.month_name[month].lower()}_{year}.txt"
with open(filename, "w") as f:
    f.write(calendar.month(year, month))