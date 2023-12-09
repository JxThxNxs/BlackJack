import random

def create_deck():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    deck = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck

def calculate_score(cards):
    score = sum([get_card_value(card['rank']) for card in cards])
    if 'A' in [card['rank'] for card in cards] and score + 10 <= 21:
        score += 10
    return score

def get_card_value(rank):
    if rank in ['J', 'Q', 'K']:
        return 10
    elif rank == 'A':
        return 1
    else:
        return int(rank)

def display_cards(cards, player_name):
    print(f"{player_name}'s cards: {', '.join([card['rank'] + ' of ' + card['suit'] for card in cards])}")

def blackjack():
    player_cards = []
    dealer_cards = []
    deck = create_deck()

    for _ in range(2):
        player_cards.append(deck.pop())
        dealer_cards.append(deck.pop())

    game_over = False

    while not game_over:
        player_score = calculate_score(player_cards)
        dealer_score = calculate_score(dealer_cards)

        display_cards(player_cards, "Player")
        print(f"Player's score: {player_score}")
        display_cards(dealer_cards, "Dealer")

        if player_score == 21 or dealer_score == 21 or player_score > 21:
            game_over = True
        else:
            draw_card = input("Do you want to draw another card? Type 'y' for yes, 'n' for no: ")
            if draw_card == 'y':
                player_cards.append(deck.pop())
            else:
                game_over = True

    while dealer_score < 17:
        dealer_cards.append(deck.pop())
        dealer_score = calculate_score(dealer_cards)

    display_cards(player_cards, "Player")
    print(f"Player's score: {player_score}")
    display_cards(dealer_cards, "Dealer")
    print(f"Dealer's score: {dealer_score}")

    if player_score == 21 or (dealer_score > 21 and player_score <= 21) or (player_score <= 21 and player_score > dealer_score):
        print("You win!")
    elif dealer_score == 21 or (player_score > 21 and dealer_score <= 21) or (dealer_score <= 21 and dealer_score > player_score):
        print("Dealer wins!")
    else:
        print("It's a draw!")

blackjack()