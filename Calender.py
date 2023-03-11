date_str = input("Please enter a date in the format dd/mm/yyyy: ")

day, month, year = date_str.split("/")

import datetime
date_obj = datetime.date(int(year), int(month), int(day))

weekday_str = date_obj.strftime("%A")

print("The weekday for the given date is:", weekday_str)
