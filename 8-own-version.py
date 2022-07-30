import datetime

print('Own version of the calendar')

DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December')

while True:
    print('What year do you want?')
    response = input('> ')

    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break
    print('Please input a valid year. f.eg. 2022')
    continue

while True:
    print('What month do you want?')
    response = input('> ')

    if response.isdecimal() and 0 < int(response) < 13:
        month = int(response)
        break
    print('Please input a valid month. f.eg. 5')
    continue

def getCalendar(month, year):
    calText = ''
    currentDate = datetime.date(year, month, 1)


    firstRows = ''
    horizontalLine = '+----------' * 7 + '+\n'
    horizontalBlank = '|          ' * 7 + '|\n'

    while currentDate.isoweekday() != 7:
        currentDate -= datetime.timedelta(days=1)

    calText += '          ' * 3 + MONTHS[month - 1] + '  ' + str(year) + '\n'
    calText += '...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..' + '\n'
    calText += horizontalLine
    days = []
    while True:
        for i in range(7):
            if len(str(currentDate.day)) == 1:
                blanks = '         '
            else:
                blanks = '        '
            firstRows += ('|' + str(currentDate.day) + blanks)
            days.append(str(currentDate))
            currentDate += datetime.timedelta(days=1)
        calText += firstRows + '|\n'
        calText += (horizontalBlank * 3 + horizontalLine)

        if str(datetime.date(year=year, month=month + 1, day=1) - datetime.timedelta(days=1)) in days:
            break
        firstRows = ''
    print(calText)

getCalendar(month, year)

