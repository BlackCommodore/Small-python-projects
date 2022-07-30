"""Calendar generator by Al Sweigart"""

import datetime

DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December')
print('Calendar generator by Al Sweigart')

while True:
    print('Write year for calendar:')
    year = input('> ')

    if year.isdecimal() and int(year) > 0:
        year = int(year)
        break

    print("Year have to be numeric, eg. 2021")

while True:
    print('Write month for calendar:')
    month = input('> ')

    if month.isdecimal() and 0 < int(month) <= 12:
        month = int(month)
        break
    print("Month have to be numeric, eg. 12")


def getCalendar(year, month):
    calText = ""

    # month and year show on the top of calendar
    calText += (' ' * 34) + MONTHS[month-1] + ' ' + str(year) + '\n'

    # show weekdays
    calText += '...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..\n'

    # horizontal line separating weeks
    weekSeparator = ('+----------' * 7) + '+\n'

    # blank rows has 10 spaces between days separators
    blankRow = ('|          ' * 7) + '|\n'

    # find first date in week
    currentDate = datetime.date(year, month, 1)

    # find sunday
    while currentDate.weekday() != 6:  # 6 is sunday, 0 is monday
        currentDate -= datetime.timedelta(days=1)  # using timedelta subtracting days by 1

    while True:  # loop for every week in month
        calText += weekSeparator

        # variable  dayNumberRow is row with numbers of days
        dayNumberRow = ''
        for i in range(7):
            dayNumberLabel = str(currentDate.day).rjust(2)
            dayNumberRow += '|' + dayNumberLabel + (' ' * 8)
            currentDate += datetime.timedelta(days=1)  # go to next day
        dayNumberRow += '|\n'  # add | after saturday

        # show row with day numbers and 3 blank rows
        calText += dayNumberRow
        for i in range(3):
            calText += blankRow

        # check if every day in month was added
        if currentDate.month != month:
            break

    # add horizontal line on bottom of calendar
    calText += weekSeparator
    return calText

calText = getCalendar(year, month)
print(calText)


