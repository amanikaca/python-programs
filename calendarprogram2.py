#using datetime module without calendar module
import datetime
month=int(input("enter the month (1-12) :"))
year=int(input("enter the year :"))


# Validate month
if 1 <= month <= 12:
    # Get first day of the month
    first_day = datetime.date(year, month, 1)
    
    # Find number of days in the month
    if month == 12:
        next_month = datetime.date(year + 1, 1, 1)
    else:
        next_month = datetime.date(year, month + 1, 1)
    
    num_days = (next_month - first_day).days

    print(f"\nCalendar for {first_day:%B %Y}") #%B for month and %Y for year in correct format
    print("Mo Tu We Th Fr Sa Su")

    # Start position
    start_day = first_day.weekday()  # Monday = 0
    print("   " * start_day, end="")

    # Print days
    for day in range(1, num_days + 1):
        print(f"{day:2} ", end="")
        if (start_day + day) % 7 == 0:
            print()
else:
    print("Invalid month. Please enter 1 to 12.")

          
#output
#C:\Users\Dell\Desktop\-\Python>py calendarprogram2.py
#enter the month (1-12) :6
#enter the year :2025

#Calendar for June 2025
#Mo Tu We Th Fr Sa Su
#                   1
# 2  3  4  5  6  7  8
# 9 10 11 12 13 14 15
#16 17 18 19 20 21 22
#23 24 25 26 27 28 29
#30