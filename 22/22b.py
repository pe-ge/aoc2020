from collections import deque

data = open("input.txt").read().split("\n\n")

def parse_raw_deck(raw_deck):
    deck = deque()
    for card in raw_deck.split("\n")[1:]:
        deck.append(int(card))

    return deck

player1_deck = parse_raw_deck(data[0])
player2_deck = parse_raw_deck(data[1])

def remember_state(previous_states, player1_deck, player2_deck):
    previous_states.add((tuple(player1_deck), tuple(player2_deck)))

def state_already_occured(previous_states, player1_deck, player2_deck):
    return (tuple(player1_deck), tuple(player2_deck)) in previous_states

def make_copy(deck, deck_length):
    copied_deck = deck.copy()
    while len(copied_deck) > deck_length:
        copied_deck.pop()
    return copied_deck

def play(player1_deck, player2_deck):
    previous_states = set()
    while player1_deck and player2_deck:
        if state_already_occured(previous_states, player1_deck, player2_deck):
            return True
        remember_state(previous_states, player1_deck, player2_deck)

        player1_card = player1_deck.popleft()
        player2_card = player2_deck.popleft()
        player1_won = False
        if len(player1_deck) >= player1_card and len(player2_deck) >= player2_card:
            player1_deck_copy = make_copy(player1_deck, player1_card)
            player2_deck_copy = make_copy(player2_deck, player2_card)
            player1_won = play(player1_deck_copy, player2_deck_copy)
        else:
            if player1_card > player2_card:
                player1_won = True

        if player1_won:
            player1_deck.append(player1_card)
            player1_deck.append(player2_card)
        else:
            player2_deck.append(player2_card)
            player2_deck.append(player1_card)

    return player1_won


play(player1_deck, player2_deck)

deck = player1_deck if player1_deck else player2_deck
print(sum(card * multiplier for (card, multiplier) in zip(deck, range(len(deck), 0, -1))))
