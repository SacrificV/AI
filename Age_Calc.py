from datetime import datetime

birth = input("Enter your birthday(YYYY-MM-DD): ")
birth_date = datetime.strptime(birth, "%Y-%m-%d")
today = datetime.today()
age = today.year - birth_date.year
if (today.month, today.day  ) < (birth_date.month, birth_date.day):
    age -= 1
print("Your age is: ", age)