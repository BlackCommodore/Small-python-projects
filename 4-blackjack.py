import random, sys

# const declaration
HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)
BACKSIDE = 'backside'


def main():
    print('Blackjack, author: Al Sweigart')
    while True:
        money = input('What starting money do you want? > ')
        if money.isdecimal() and int(money) > 0:
            money = int(money)
            break
    while True:
        # Check if player has money
        if money <= 0:
            print("You are a bankrupt!")
            print("Thank you for playing")
            sys.exit()

        # bet stage
        print("Bugdet:", money)
        bet = getBet(money)

        # give croupier and player two cards each from deck
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        # player move
        print('Bet: ', bet)
        while True:  # loop till player won't take another card or get over 21
            displayHands(playerHand, dealerHand, False)
            print()

            # check if player has over 21 points
            if getHandValue(playerHand) >= 21:
                break
            # read player move, S or D
            move = getMove (playerHand, money - bet)

            if move == 'D':
                # player doubles bet
                additionalBet = getBet(min(bet, (money - bet)))
                bet += additionalBet
                print(f'Bet increased to {bet}')
                print(f'Bet: {bet}')

            if move in ('T', 'D'):
                # take another card
                newCard = deck.pop()
                rank, suit = newCard
                print(f'You took {rank} {suit}')
                playerHand.append(newCard)

                if getHandValue(playerHand) > 21:
                    # value ovwr 21
                    continue

            if move in ('S', 'D'):
                # end of turn
                break

        # croupier move
        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                # croupier get another card
                print('Croupier take another card...')
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)
                if getHandValue(dealerHand) > 21:
                    break  # croupier has over 21 points
                input('Press enter to continue...')
                print('\n\n')

        # Showing cards on hand
        displayHands(playerHand, dealerHand, True)

        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)

        # winner checking
        if dealerValue > 21:
            print(f'Croupier got over 21 points! You won {bet} USD!')
            money += bet
        elif (playerValue > 21) or (playerValue < dealerValue):
            print('You lose!')
            money -= bet
        elif playerValue > dealerValue:
            print(f'You won {bet} USD!')
            money += bet
        elif playerValue == dealerValue:
            print(f'Draw, bet comes back to you')

        input('Press enter to continue...')
        print('\n\n')


def getBet(maxBet):
    """ask player what is the bet"""
    while True:  # ask him till he will give correct data
        print(f'What is your bet? (1-{maxBet} or END)')
        bet = input('> ').upper().strip()  # capitalized and striped for spaces
        if bet == 'END':
            print('Thank you for playing!')
            sys.exit()

        if not bet.isdecimal():
            if bet == 0:
                print('Type END if you want to quit')
                continue
            print(f'Only numbers! (from 1 to {maxBet} or END)')
            continue  # if input is not number, ask again

        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet  # player gave correct value


def getDeck():
    """give tuple of every 52 cards (rank, suit)"""
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))  # appending numeric cards
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit))  # appending figures and aces
    random.shuffle(deck)
    return deck


def displayHands(playerHand, dealerHand, showDealerHand):
    """Showing player and croupier hand. Firstly hide croupier cards (var showDealerHand == False)"""
    print()
    if showDealerHand:
        print('Croupier: ', getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print('Croupier: ???')
        # firstly hide croupier hand
        displayCards([BACKSIDE] + dealerHand[1:])

    # showing players cards
    print('Player: ', getHandValue(playerHand))
    displayCards(playerHand)


def getHandValue(cards):
    """Returns card value. Figures = 10, aces 11 or 1 (this function chooses the most appropriate ace value)"""
    value = 0
    numberOfAces = 0

    # summing cards without aces
    for card in cards:
        rank = card[0]  # card is a tuple (rank, suit)
        if rank == 'A':
            numberOfAces += 1
        elif rank in ('K', 'Q', 'J'):  # 10 points figures
            value += 10
        else:
            value += int(rank)  # adding number from card

    # adding aces value
    value += numberOfAces  # adding 1
    for i in range(numberOfAces):
        # if you can add 10 points more from ace without exceeding 21, do it
        if value + 10 <= 21:
            value += 10

    return value


def displayCards(cards):
    """Showing all cards from list"""
    rows = ['', '', '', '', '----------------------------------------']  # txt showing in each row

    for i, card in enumerate(cards):
        rows[0] += ' ___ '  # top edge of card
        if card == BACKSIDE:
            # shows backside of card
            rows[1] += '|## |'
            rows[2] += '|###|'
            rows[3] += '|_##|'
        else:
            # showing front of card
            rank, suit = card  # card is a tuple
            rows[1] += f'|{rank.ljust(2)} |'
            rows[2] += f'| {suit} |'
            rows[3] += f'|_{rank.rjust(2, "_")}|'

    # showing every row in screen
    for row in rows:
        print(row)


def getMove(playerHand, money):
    """Ask player for next move, return 'T' if taking another card and 'S' if he do not want another card.
    'D' for double bet"""
    while True: # do the loop till correct answer
        # determine players choices
        moves = ['(T)ake another', '(S)top']

        # player can double bet in first move
        # when he has two cards
        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble')

        # read player move
        movePrompt = ', '.join(moves) + '> '
        move = input(movePrompt).upper()
        if move in ('T', 'S'):
            return move  # player write correct value
        if move == 'D' and '(D)ouble' in moves:
            return move  # player write correct value


if __name__ == '__main__':
    main()