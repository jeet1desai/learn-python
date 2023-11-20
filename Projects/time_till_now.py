from datetime import datetime

format_of_date = "%d.%m.%Y"

deadline_time = input("Please enter time in this format DD.MM.YYYY : ")

deadline_date = datetime.strptime(deadline_time, format_of_date)
# print(deadline_date)

today_date = datetime.now()
# print(today_date)

time_remaining = deadline_date - today_date
print(f"Time remaining {time_remaining.days} days.")