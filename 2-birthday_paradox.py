import datetime, random


def getbirthdays(number_of_birthdays):
    """Returns number of random birthdays"""
    birthdays = []
    for _ in range(number_of_birthdays):
        # Year is no important in this simulation
        startofyear = datetime.date(2001, 1, 1)

        # Random day of the year:
        randomnuberofdays = datetime.timedelta(days=random.randint(0, 364))  # Time delta - number of days
        birthday = startofyear + randomnuberofdays  # Move day form the first jan of 2021
        birthdays.append(birthday)
    return birthdays


def getmatch(birthdays):
    """Returns birthday dates, which appeared more than once in birthdays list"""
    if len(birthdays) == len(set(birthdays)):
        return None  # Every day is unique (list is equal to set)

    # Compare every birthday with others
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1 :]):
            if birthdayA == birthdayB:
                return birthdayA  # Return the same birthdays


# Show introduction:
print('''Paradoks dnia urodzin, autor: Al Sweigart, al@inventwithpython.com
Paradoks dnia urodzin pokazuje, że w grupie N osób szansa,
że dwie osoby mają urodziny w tym samym dniu, jest zaskakująco duża.
Ten program wykorzystuje metodę Monte Carlo (czyli powtarzalne losowe symulacje),
by ustalić to prawdopodobieństwo.''')

# Tuple with months names:
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True: # Ask until user put correct values
    print('How many birthdays should I generate? (Max. 100)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):  # Response is decimal number and between 0 nad 100
        numbdays = int(response)
        break  # User put correct values
print()

# Generate and print days of birth:
print(f'This are {numbdays} days of birth: ')
birthdays = getbirthdays(numbdays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        # After first birthday put comma
        print(', ', end='')
    monthname = MONTHS[birthday.month - 1]
    datetext = f'{monthname} {birthday.day}'
    print(datetext, end='')
print()
print()

# Checking if there are the same days of birth
match = getmatch(birthdays)

# Wyświetl wyniki:
print('In this imulation, ', end='')
if match != None:
    monthname = MONTHS[match.month - 1]
    datetext = f'{monthname} {match.day}'
    print('few people has birthadys', datetext)
else:
    print('There are no the same birth days')
print()

# Made 100 000 simulations
print(f'Generating {numbdays} random birth days 100 000 times...')
input('Press enter to start...')

print('Proceeding another 100 000 simulations.')
simmath = 0  # Number of simulations in which appeared the same birthdays
for i in range(100_000):
    # Printing progress every 10 000 simulations:
    if i % 10_000 == 0:
        print(f'{i} simulations carried out...')
    birthdays = getbirthdays(numbdays)
    if getmatch(birthdays) != None:
        simmath += 1
print('100 000 simulations carried out.')

# Printing results of simulations
probability = round(simmath / 100_000 * 100, 2)
print(f'Ze 100 000 symulacji dla {numbdays} osób, ten sam')
print(f'dzień urodzin wystąpił {simmath} razy. Oznacza to,')
print(f'że dla {numbdays} ludzi istnieje {probability} szans, iż')
print(f'dwie lub więcej osób będzie miało urodziny w tym samym dniu.')
print(f'To prawdopodobnie więcej niż przypuszczałeś!')

