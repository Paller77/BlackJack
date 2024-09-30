import random
from art import logo


##Programmer defined functions:
def deal_cards():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and calculates the score of the hands"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "DRAW!"
    elif c_score == 0:
        return "Dealer has BlackJack! You Lost!"
    elif u_score == 0:
        return "Player has BlackJack! You Won!"
    elif u_score > 21:
        return "You went over! You Lost!"
    elif c_score > 21:
        return "Dealer went over! You Won!"
    elif u_score > c_score:
        return "You Won!"
    else:
        return "You Lost!"

## THE GAME
def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Do you hit or stand? ('h' or 's')\n")
            if user_should_deal == "h":
                user_cards.append(deal_cards())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}\nYour final score: {user_score}")
    print(f"Dealer's final hand: {computer_cards}\nDealer's final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play BlackJack? ;) ('y' or 'n')") == "y":
    print("\n"*20)
    play_game()