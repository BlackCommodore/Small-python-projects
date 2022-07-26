import random


def main():
    num_digits, max_guess = selectoptions()
    powitanie(num_digits)
    while True:  # Pętla główna
        secretNum = getSecretNum(num_digits)  # Ta zmienna przechowuje liczbę, którą gracz musi odgadnąć
        print('Mam na myśli liczbę.')
        print(f'Masz {max_guess} prób, by odgadnąć, jaka to liczba.')

        numGuesses = 1
        while numGuesses <= max_guess:
            guess = ''
            # Wykonywanie pętli, dopóki gracz nie poda poprawnej liczby
            while len(guess) != num_digits or not guess.isdecimal():
                print(f'Próba #{numGuesses}')
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break  # Podana liczba jest poprawna, zakońćż pętlę
            if numGuesses > max_guess:
                print('Wykorzystałeś wszystkie próby.')
                print(f'Prawidłowa odpowiedź to: {secretNum}.')

        # Zapytaj gracza czy chce zagrać ponownie
        print('Czy chcesz zagrać jescze raz? (tak lub nie)')
        if not input('> ').lower().startswith('t'):
            break
        else:
            num_digits, max_guess = selectoptions()
            powitanie(num_digits)
    print('Dziękuję za grę!')


def powitanie(num_digits):
    print(f'''Bajgle - logiczna gra na dedukcję                                            
    Mam na myśli {num_digits}-cyfrową liczbę, w której nie powtarza się żadna z cyfr.          
    Spróbuj ją odgadnąć. Oto wskazówki:                                                        
    Gdy mówię:      Oznacza to:                                                                
    znajduje się            Jedna z cyfr jest poprawna, ale jest na złej pozycji.          
    jest na miejscu         Jedna z cyfr jest poprawna i znajduje się w odpowiednim miejscu
    kumbak                  Żadna cyfra nie jest poprawna.''')


def selectoptions():
    num_digits = int(input("Ile cyfr ma mieć szukana liczba? (10 maksymalnie): "))
    max_guess = int(input("W ilu próbach zdołasz zgadnąć? "))
    return num_digits, max_guess


def getSecretNum(num_digits):
    """Zwraca liczbę złożoną z tylu losowych, unikatowyh cyfr, ile wynosi wartość NUM_DIGITS"""
    numbers = list('0123456789')  # Utwórz listę cyfr od 0 do 9
    random.shuffle(numbers)  # Ustaw je w losowej kolejności

    # Dodaj kolejne cyfry do tajemnej liczby
    secretNum = ''
    for i in range(num_digits):
        secretNum += (numbers[i])
    return secretNum


def getClues(guess, secretNum):
    """Zwraca łańcuch znaków piko, fermi, bajgle dla danej próby
    lub informację o wygranej"""
    if guess == secretNum:
        return 'Udało się!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # Poprawna cyfra w odpowiednim miejscu
            clues.append('jest na miejcu')
        elif guess[i] in secretNum:
            # Poprawna cyfra w złym miejscu
            clues.append('znajduje się')
    if len(clues) == 0:
        return "kumbak"  # Brak poprawnych cyfr
    else:
        # Ustaw wskazówki w kolejności alfabetycznej by ich kolejność nie zdradzała zbyt wielu informacji.
        clues.sort()
        # Wszystkie wskazówki połącz w jeden łańcuch znaków
        return " - ".join(clues)

# Jeżeli program został uruchomiony a nie zaimportowany to uruchom grę


if __name__ == '__main__':
    main()