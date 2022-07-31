import datetime, sys

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
    holidays = [f'{year}-08-15', f'{year}-01-01', f'{year}-01-06', f'{year}-04-17', f'{year}-05-01', f'{year}-05-03',
                f'{year}-06-05', f'{year}-06-16', f'{year}-11-01', f'{year}-11-11', f'{year}-12-25', f'{year}-12-26']
    firstRows = ''
    horizontalLine = '+----------' * 7 + '+\n'
    horizontalBlank = '|          ' * 7 + '|\n'


    while currentDate.isoweekday() != 7:
        currentDate -= datetime.timedelta(days=1)

    calText += '          ' * 3 + MONTHS[month - 1] + '  ' + str(year) + '\n'  # print on top month and year
    calText += '...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..' + '\n'
    calText += horizontalLine
    holidayMarker = ' '
    while True:
        for i in range(7):
            if str(currentDate) in holidays:
                holidayMarker = 'H'
            if len(str(currentDate.day)) == 1:
                blanks = f'       {holidayMarker} '
            else:
                blanks = f'      {holidayMarker} '
            firstRows += ('|' + str(currentDate.day) + blanks)
            currentDate += datetime.timedelta(days=1)
            holidayMarker = ' '
        calText += firstRows + '|\n'
        calText += (horizontalBlank * 3 + horizontalLine)

        if month != currentDate.month:
            break
        firstRows = ''
    return calText

createdCalendar = getCalendar(month, year)
print(createdCalendar)

print('Do you want to save calendar to txt file? (yes or no)')
answer = input('> ').lower()
if answer.startswith('y'):
    with open(f'calendar_{month}-{year}.txt', 'w') as calendar:
        calendar.write(createdCalendar)
        print(f"File saved as {calendar}")
sys.exit()

