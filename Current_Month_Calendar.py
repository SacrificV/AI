import calendar
from datetime import datetime
now = datetime.now()
print(calendar.month(now.year, now.month))