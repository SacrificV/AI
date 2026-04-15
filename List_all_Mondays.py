import calendar
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
print("Mondays: ")
cal = calendar.monthcalendar(year, month)
for week in cal:
    if week[0] != 0:
        print(f"{year}-{month:02d}-{week[0]:02d}")