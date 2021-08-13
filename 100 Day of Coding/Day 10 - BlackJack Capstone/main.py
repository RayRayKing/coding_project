## BlackJack Game in Text through terminal

#program initalization
import random 
deck = [11,2,3,4,5,6,7,8,9,10,10,10,10]*4
# draw cards and put into list
def draw(hand):
    """Deal a card to one person"""
    idx = random.randrange(0,len(deck)-1)
    hand.append(deck.pop(idx))
    return hand
    # if hand == player_hand:
    #     print(f"You new hand is :{hand}")
    # elif hand == dealer_hand and len(hand)<2:
    #     print(f"Dealer Hand is {hand}")
    # return hand
## Calculate score
def calc(hand):
    total = 0
    for card in hand:
        total += card
        if total > 21 and 11 in hand:
            total -= 10
            hand.remove(11)
            hand.append(1)
    return total

#Game start
def play():
    player_hand = list()
    p_score = 0
    dealer_hand = list()
    d_score = 0

    play_game = True
    draw(player_hand)
    draw(dealer_hand)
    draw(player_hand)
    draw(dealer_hand)
    p_score = calc(player_hand)
    d_score = calc(dealer_hand)
    print(f"You new hand is :{player_hand}")
    print(f"Dealer has : "+ str(dealer_hand[0]))


    print
    #first had blackjack score
    if p_score == d_score and p_score == 21:
        print("Tie! Two blackjack on first draw!")
        play_game = False
    elif p_score == 21:
        print("User has Black Jack. User Wins, Dealer Loses!")
        print(f"User has {player_hand}. Dealer has {dealer_hand}")
        play_game = False
    elif d_score == 21:
        print("Dealer has Black Jack. Dealer Wins, User Loses!")
        print(f"User has {player_hand}. Dealer has {dealer_hand}")
        play_game = False


    while play_game:
        #User turn
        ans = input("hit or stay?")
        while ans == "hit":
            draw(player_hand)
            p_score = calc(player_hand)
            print(f"You have {p_score}")
            if p_score > 21:
                print("User busts game over!")
                play_game = False
                break
            ans = input("hit or stay?")


        #dealer turn
        while d_score < 16:
            draw(dealer_hand)
            d_score = calc(dealer_hand)
            print(f"Dealer have {d_score}")
            if d_score > 21:
                print("Dealer busts game over!")
                play_game = False
                break
            print(d_score)

        if p_score > d_score:
            print("User Wins!")
            print(f"User has {player_hand}. Dealer has {dealer_hand}")
        else:
            print("Dealer wins")
            print(f"User has {player_hand}. Dealer has {dealer_hand}")
        play_game = False
        

while input("play_again Y/N") == "Y":
    play()