from datetime import datetime

def isLeap(y):
    return ((y % 400 == 0) and (y % 100 == 0)) or ((y % 4 == 0) and (y % 100 != 0))

for yr in range(1006, 1996, 10):
    if datetime(yr, 1, 26).weekday() == 0 and isLeap(yr):
        print(yr)

# this challenge sucks
# jan 27 1756 - mozart birthday
