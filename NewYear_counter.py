from datetime import datetime

today = datetime.today()
next_year = datetime(today.year + 1, 1, 1)
days = (next_year - today).days
print("Days until New Year: ",days)