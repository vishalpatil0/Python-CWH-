#calender programme

import calendar 



print("Your Calender\n \n ")



y = int(input("Enter the Year : "))

m = int(input("Enter the month : "))



mycalender = calendar.month(y , m)

print("\n", mycalender) 