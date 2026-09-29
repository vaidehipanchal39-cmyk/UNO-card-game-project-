import random

# Color codes for ANSI terminal output
colorCodes = {
    'red': '\033[1;31m',
    'green': '\033[1;32m',
    'blue': '\033[1;34m',
    'yellow': '\033[1;33m',
    'reset': '\033[0m'
}

# Card values and colors
values = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'Skip', 'Reverse', 'Draw2']
colors = ['red', 'green', 'blue', 'yellow']
wildCards = ['Wild', 'WildDraw4']

def getCardInfo(card_str):
    for color in colors:
        if card_str.startswith(color):
            return color, card_str[len(color):]
    if card_str in wildCards:
        return None, card_str
    return None, card_str

def build_deck():
    deck = []
    for color in colors:
        for value in values:
            deck.append(f"{color}{value}")
            if value != '0':
                deck.append(f"{color}{value}")
    for _ in range(4):
        for wildCardType in wildCards:
            deck.append(wildCardType)
    random.shuffle(deck)
    return deck

def dealHands(deck, numPlayers=2, cardPerPlayer=7):
    hands = {"You": [], "Computer": []}
    for _ in range(cardPerPlayer):
        for playerName in hands:
            hands[playerName].append(deck.pop())
    return hands, deck

def isValidMove(card, top_card):
    cardColor, cardVal = getCardInfo(card)
    topColor, topVal = getCardInfo(top_card)
    if cardVal in wildCards:
        return True
    return (cardColor is not None and cardColor == topColor) or \
           (cardVal is not None and topVal is not None and cardVal == topVal)

def playColabUno():
    deck = build_deck()
    hands, deck = dealHands(deck)
    discardPile = [deck.pop()]
    
    # Avoid starting with a wild card for fair start
    while discardPile[-1] in wildCards:
        deck.append(discardPile.pop())
        random.shuffle(deck)
        discardPile.append(deck.pop())

    print("=" * 35)
    print("      LET'S START UNO GAME!        ")
    print("=" * 35)

    startCardColor, _ = getCardInfo(discardPile[-1])
    print(f"Starting card on table: {colorCodes.get(startCardColor, colorCodes['reset'])}{discardPile[-1]}{colorCodes['reset']}\n")
    currentTurn = "You"

    while True:
        # Reshuffle if deck is low
        if len(deck) < 5 and len(discardPile) > 1:
            top = discardPile.pop()
            deck = list(discardPile)
            random.shuffle(deck)
            discardPile = [top]
            print("\n[INFO] Deck reshuffled from discard pile.")

        topCard = discardPile[-1]

        # Check win conditions
        if not hands["You"]:
            print("\n" + "=" * 40)
            print("  CONGRATULATIONS! YOU WON THE GAME!  ")
            print("=" * 40)
            break

        if not hands["Computer"]:
            print("\n" + "=" * 40)
            print("   GAME OVER! COMPUTER WON THE GAME.  ")
            print("=" * 40)
            break

        if currentTurn == "You":
            print("-" * 35)
            topCardColor, _ = getCardInfo(topCard)
            print(f"Top card on table : {colorCodes.get(topCardColor, colorCodes['reset'])}{topCard}{colorCodes['reset']}")
            print(f"Computer has {len(hands['Computer'])} cards left.")
            print("Your current hand :")
            for idx, card in enumerate(hands["You"]):
                cColor, _ = getCardInfo(card)
                print(f"  {idx + 1}. {colorCodes.get(cColor, colorCodes['reset'])}{card}{colorCodes['reset']}")

            playable = [c for c in hands["You"] if isValidMove(c, topCard)]
            print("\nOptions: Enter card number to play, or 'D' to draw.")
            choice = input("Your choice: ").strip()

            if choice.upper() == 'D':
                if not deck and len(discardPile) > 1:
                    top = discardPile.pop()
                    deck = list(discardPile)
                    random.shuffle(deck)
                    discardPile = [top]

                if deck:
                    draw = deck.pop()
                    hands["You"].append(draw)
                    dColor, _ = getCardInfo(draw)
                    print(f"You drew: {colorCodes.get(dColor, colorCodes['reset'])}{draw}{colorCodes['reset']}")
                    if isValidMove(draw, topCard):
                        print(f"You automatically played your drawn card: {draw}")
                        hands["You"].remove(draw)
                        discardPile.append(draw)
                        _, drawnVal = getCardInfo(draw)
                        if "Skip" in drawnVal or "Reverse" in drawnVal:
                            print("Action card played! You get another turn.")
                            currentTurn = "You"
                            continue
                        elif "Draw2" in drawnVal:
                            print("Computer draws 2 cards! You get another turn.")
                            for _ in range(2):
                                if deck: hands["Computer"].append(deck.pop())
                            currentTurn = "You"
                            continue
                        elif "WildDraw4" in drawnVal:
                            print("Computer draws 4 cards! You get another turn.")
                            for _ in range(4):
                                if deck: hands["Computer"].append(deck.pop())
                            currentTurn = "You"
                            continue
                currentTurn = "Computer"
            else:
                try:
                    idx = int(choice) - 1
                    if idx < 0 or idx >= len(hands["You"]):
                        print("Invalid selection! Index out of range.")
                        continue
                    chosenCard = hands["You"][idx]

                    if chosenCard in playable:
                        hands["You"].remove(chosenCard)
                        discardPile.append(chosenCard)
                        print(f"\nYou played: {chosenCard}")

                        _, chosenCardVal = getCardInfo(chosenCard)

                        if "Skip" in chosenCardVal or "Reverse" in chosenCardVal:
                            print("Action card! You get another turn.")
                            currentTurn = "You"
                        elif "Draw2" in chosenCardVal:
                            print("Computer draws 2 cards! You get another turn.")
                            for _ in range(2):
                                if deck: hands["Computer"].append(deck.pop())
                            currentTurn = "You"
                        elif "WildDraw4" in chosenCardVal:
                            print("Wild Draw 4! Computer draws 4 cards and skips.")
                            for _ in range(4):
                                if deck: hands["Computer"].append(deck.pop())
                            currentTurn = "You"
                        else:
                            currentTurn = "Computer"
                    else:
                        print("Invalid card! It does not match the top card's color or value.")
                except ValueError:
                    print("Invalid input! Please enter a number or 'D'.")

        elif currentTurn == "Computer":
            print("-" * 35)
            print("Computer is thinking...")
            computerPlayable = [c for c in hands["Computer"] if isValidMove(c, topCard)]

            if not computerPlayable:
                if not deck and len(discardPile) > 1:
                    top = discardPile.pop()
                    deck = list(discardPile)
                    random.shuffle(deck)
                    discardPile = [top]

                if deck:
                    draw = deck.pop()
                    hands["Computer"].append(draw)
                    print(f"Computer drew a card.")
                    if isValidMove(draw, topCard):
                        hands["Computer"].remove(draw)
                        discardPile.append(draw)
                        print(f"Computer automatically played its drawn card: {draw}")
                        _, drawnVal = getCardInfo(draw)
                        if "Skip" in drawnVal or "Reverse" in drawnVal:
                            print("Computer played an action card! It gets another turn.")
                            currentTurn = "Computer"
                            continue
                        elif "Draw2" in drawnVal:
                            print("You must draw 2 cards! Computer gets another turn.")
                            for _ in range(2):
                                if deck: hands["You"].append(deck.pop())
                            currentTurn = "Computer"
                            continue
                        elif "WildDraw4" in drawnVal:
                            print("Computer played Wild Draw 4! You draw 4 cards.")
                            for _ in range(4):
                                if deck: hands["You"].append(deck.pop())
                            currentTurn = "Computer"
                            continue
                currentTurn = "You"
            else:
                chosenCard = computerPlayable[0]
                hands["Computer"].remove(chosenCard)
                discardPile.append(chosenCard)
                print(f"Computer played: {chosenCard}")

                _, chosenCardVal = getCardInfo(chosenCard)
                if "Skip" in chosenCardVal or "Reverse" in chosenCardVal:
                    print("Computer played an action card! It gets another turn.")
                    currentTurn = "Computer"
                elif "Draw2" in chosenCardVal:
                    print("You must draw 2 cards! Computer gets another turn.")
                    for _ in range(2):
                        if deck: hands["You"].append(deck.pop())
                    currentTurn = "Computer"
                elif "WildDraw4" in chosenCardVal:
                    print("Computer played Wild Draw 4! You draw 4 cards.")
                    for _ in range(4):
                        if deck: hands["You"].append(deck.pop())
                    currentTurn = "Computer"
                else:
                    currentTurn = "You"

if __name__ == "__main__":
    playColabUno()
