import random

def player_move(my_deck):
    my_hand_value = sum(my_deck)
    print(f"Your cards: {my_deck}, current score: {my_hand_value}")
    return my_hand_value

def handle_defeat(deck, score, dealer):
    print(f"Your final hand: {deck}, final score: {score}")
    print(f"Dealer's final hand: {dealer}, final score: {sum(dealer)}")
    print("You went over. You lose 😭")

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

while True:
    wannaPlay = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ").lower()
    if wannaPlay == 'y':
        my_deck = []
        dealer_hand = []
        
        # Cartas iniciais
        for i in range(2):
            my_deck.append(random.choice(cards))
        my_hand_value = player_move(my_deck)
        
        dealer_hand.append(random.choice(cards))
        print(f"Dealer's first hand: {dealer_hand[0]}")
        
        # Turno do jogador
        while True:
            wannaPass = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if wannaPass == 'y':
                my_deck.append(random.choice(cards))
                my_hand_value = player_move(my_deck)
                
                if my_hand_value > 21:
                    handle_defeat(my_deck, my_hand_value, dealer_hand)
                    break
            else:
                # Turno do dealer
                while sum(dealer_hand) < 17:
                    dealer_hand.append(random.choice(cards))
                
                dealer_score = sum(dealer_hand)
                print(f"Your final hand: {my_deck}, final score: {my_hand_value}")
                print(f"Dealer's final hand: {dealer_hand}, final score: {dealer_score}")
                
                if dealer_score > 21:
                    print("Dealer went over. You Win! 🎉")
                elif dealer_score > my_hand_value:
                    print("You lose 😭")
                elif dealer_score == my_hand_value:
                    print("Draw 🤝")
                else:
                    print("You Win! 🎉")
                break
    else:
        print("Exiting BlackJack, see you soon 👋")
        break