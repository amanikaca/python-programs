#using calendar module
import calendar
month=int(input("enter the month(1-12) :"))
year=int(input("enter the year : "))

if 1<= month <12:
    print(" calender")
    print(calendar.month(year,month))
else:
    print("invalid month.please enter a correct month(1-12)")

    #output
# C:\Users\Dell\Desktop\-\Python>py calendarprogram.py
#enter the month(1-12) :5
#enter the year : 2003
 #calender
 #    May 2003
# Mo Tu We Th Fr Sa Su
#           1  2  3  4
# 5   6  7  8  9 10 11
# 12 13 14 15 16 17 18
# 19 20 21 22 23 24 25
# 26 27 28 29 30 31


