#Input : Year and Month
#Output: Calendar of that month of that year

import calendar
y = int(input("Enter the year : "))
m = int(input("Enter the month number: "))
if m > 12:
    print("Try entering a valid month number")
else:
    print(calendar.month(y, m))
