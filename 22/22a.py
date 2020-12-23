from collections import deque

data = open("input.txt").read().split("\n\n")

def parse_raw_deck(raw_deck):
    deck = deque()
    for card in raw_deck.split("\n")[1:]:
        deck.append(int(card))

    return deck

player1_deck = parse_raw_deck(data[0])
player2_deck = parse_raw_deck(data[1])

while player1_deck and player2_deck:
    player1_card = player1_deck.popleft()
    player2_card = player2_deck.popleft()

    if player1_card > player2_card:
        player1_deck.append(player1_card)
        player1_deck.append(player2_card)
    else:
        player2_deck.append(player2_card)
        player2_deck.append(player1_card)

deck = player1_deck if player1_deck else player2_deck
print(sum(card * multiplier for (card, multiplier) in zip(deck, range(len(deck), 0, -1))))
