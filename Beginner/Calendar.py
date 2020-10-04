#Input : Year and Month
#Output: Calendar of that month of that year

import calendar
y = int(input("Enter the year : "))
m = int(input("Enter the month number: "))
print(calendar.month(y,m))
