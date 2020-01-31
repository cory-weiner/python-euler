
# Python datetime module makes this easy.
import datetime
def solution():
    startdate = datetime.datetime(1901, 1, 1)
    endate = datetime.datetime(2000, 12, 31)
    sundays = 0
    while startdate <= endate:
        wkday = startdate.weekday()
        if wkday == 6 and startdate.day ==1:
            sundays += 1
        startdate = startdate + datetime.timedelta(1)
    return sundays

print(solution())

    