from random import randint  # random number generator -https://programming-25.mooc.fi/part-7/2-randomness
hand = 0
while hand < 22:
    z = randint(1, 10)
    hand += z

    if hand == 21:
        print("you win!")
        break
    elif hand < 21:
        print("the game is still going")
        print(hand)
    else:
        print("you lose!")
        print(hand)
        break

# this is a very simply coded game of blackjack
# break statement needed on line 9. if not, the user gets the win text immediately followed by the lose text. game needs to end if you win.
