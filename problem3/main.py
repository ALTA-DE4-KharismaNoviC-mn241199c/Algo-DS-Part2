def playing_domino(cards, deck):
    if not cards or not deck:
        return []

    for card in cards:
        for domino in deck:
            if card == domino:
                return [card]
            elif card[0] == domino[1] or card[1] == domino[0]:
                return [card, domino]

    return []

if __name__ == "__main__":
    print(playing_domino([[6, 5], [3, 4], [2, 1], [3, 3]], [4, 3]))  # [3, 4]
    print(playing_domino([[6, 5], [3, 3], [3, 4], [2, 1]], [3, 6]))  # [6, 5]
    print(playing_domino([[6, 6], [2, 4], [3, 6]], [5, 1]))         # []