import random


# -----------------------------
# CARD DECK
# -----------------------------

suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

ranks = [
    "2", "3", "4", "5", "6", "7", "8", "9", "10",
    "J", "Q", "K", "A"
]


def create_deck():
    deck = []

    for suit in suits:
        for rank in ranks:
            deck.append((rank, suit))

    random.shuffle(deck)

    return deck


# -----------------------------
# CARD VALUE
# -----------------------------

def card_value(card):
    rank = card[0]

    if rank in ["J", "Q", "K"]:
        return 10

    elif rank == "A":
        return 11

    else:
        return int(rank)


# -----------------------------
# CALCULATE HAND VALUE
# -----------------------------

def hand_value(hand):

    total = 0
    aces = 0

    for card in hand:

        total += card_value(card)

        if card[0] == "A":
            aces += 1

    # Convert Ace from 11 to 1
    # if total is greater than 21

    while total > 21 and aces > 0:

        total -= 10
        aces -= 1

    return total


# -----------------------------
# DISPLAY CARDS
# -----------------------------

def display_hand(name, hand, hide_first_card=False):

    print(f"\n{name}'s Hand:")

    for i, card in enumerate(hand):

        rank, suit = card

        if hide_first_card and i == 0:
            print("  [Hidden Card]")
        else:
            print(f"  {rank} of {suit}")

    if not hide_first_card:

        print(f"Total: {hand_value(hand)}")


# -----------------------------
# CHECK BLACKJACK
# -----------------------------

def is_blackjack(hand):

    return len(hand) == 2 and hand_value(hand) == 21


# -----------------------------
# PLAYER TURN
# -----------------------------

def player_turn(deck, player_hand):

    while True:

        value = hand_value(player_hand)

        print(f"\nYour total: {value}")

        if value > 21:

            print("You busted!")

            return False

        if value == 21:

            print("You have 21!")

            return True

        choice = input("\nDo you want to Hit or Stand? ").lower()

        if choice == "hit":

            new_card = deck.pop()

            player_hand.append(new_card)

            print(
                f"\nYou received: "
                f"{new_card[0]} of {new_card[1]}"
            )

            display_hand("Player", player_hand)

        elif choice == "stand":

            print("\nYou chose to stand.")

            return True

        else:

            print("Invalid choice. Please type Hit or Stand.")


# -----------------------------
# DEALER TURN
# -----------------------------

def dealer_turn(deck, dealer_hand):

    print("\nDealer's turn...")

    display_hand("Dealer", dealer_hand)

    while hand_value(dealer_hand) < 17:

        new_card = deck.pop()

        dealer_hand.append(new_card)

        print(
            f"\nDealer draws: "
            f"{new_card[0]} of {new_card[1]}"
        )

        display_hand("Dealer", dealer_hand)

    dealer_value = hand_value(dealer_hand)

    if dealer_value > 21:

        print("\nDealer busted!")

    else:

        print(f"\nDealer stands at {dealer_value}.")


# -----------------------------
# DETERMINE WINNER
# -----------------------------

def determine_winner(player_hand, dealer_hand):

    player_value = hand_value(player_hand)
    dealer_value = hand_value(dealer_hand)

    print("\n" + "=" * 40)
    print("FINAL RESULT")
    print("=" * 40)

    display_hand("Player", player_hand)
    display_hand("Dealer", dealer_hand)

    # Player bust
    if player_value > 21:

        print("\nYou lose!")

        return "lose"

    # Dealer bust
    if dealer_value > 21:

        print("\nDealer busted. You win!")

        return "win"

    # Compare values
    if player_value > dealer_value:

        print("\nYou win!")

        return "win"

    elif player_value < dealer_value:

        print("\nDealer wins!")

        return "lose"

    else:

        print("\nIt's a draw!")

        return "draw"


# -----------------------------
# PLAY ONE ROUND
# -----------------------------

def play_round(balance):

    print("\n")
    print("=" * 50)
    print("NEW BLACKJACK ROUND")
    print("=" * 50)

    # Ask for bet

    while True:

        print(f"\nYour balance: ${balance}")

        try:

            bet = int(input("Enter your bet: $"))

            if bet <= 0:

                print("Bet must be greater than 0.")

            elif bet > balance:

                print("You don't have enough chips.")

            else:

                break

        except ValueError:

            print("Please enter a valid number.")

    # Create deck

    deck = create_deck()

    # Create hands

    player_hand = [
        deck.pop(),
        deck.pop()
    ]

    dealer_hand = [
        deck.pop(),
        deck.pop()
    ]

    # Show initial cards

    print("\nInitial cards:")

    display_hand("Player", player_hand)

    display_hand(
        "Dealer",
        dealer_hand,
        hide_first_card=True
    )

    # Check for Blackjack

    player_blackjack = is_blackjack(player_hand)
    dealer_blackjack = is_blackjack(dealer_hand)

    if player_blackjack:

        print("\nBLACKJACK!")

        if dealer_blackjack:

            print("Dealer also has Blackjack.")
            print("Push! Your bet is returned.")

            return balance

        else:

            winnings = int(bet * 1.5)

            print(
                f"You win ${winnings}!"
            )

            return balance + winnings

    if dealer_blackjack:

        print("\nDealer has Blackjack!")
        print("You lose your bet.")

        return balance - bet

    # Player turn

    player_alive = player_turn(
        deck,
        player_hand
    )

    if not player_alive:

        return balance - bet

    # Dealer turn

    dealer_turn(
        deck,
        dealer_hand
    )

    # Determine winner

    result = determine_winner(
        player_hand,
        dealer_hand
    )

    if result == "win":

        balance += bet

    elif result == "lose":

        balance -= bet

    # Draw = no balance change

    return balance


# -----------------------------
# MAIN GAME
# -----------------------------

def main():

    balance = 1000

    print("=" * 50)
    print("        ♠ BLACKJACK ♥")
    print("=" * 50)

    print("\nWelcome to Blackjack!")

    while balance > 0:

        balance = play_round(balance)

        print(
            f"\nYour current balance: ${balance}"
        )

        if balance <= 0:

            print("\nYou are out of chips!")
            break

        play_again = input(
            "\nPlay another round? (yes/no): "
        ).lower()

        if play_again != "yes":

            break

    print("\n" + "=" * 50)
    print("GAME OVER")
    print("=" * 50)

    print(f"Final balance: ${balance}")

    if balance > 1000:

        print("Congratulations! You made a profit.")

    elif balance == 1000:

        print("You finished where you started.")

    else:

        print("Better luck next time!")


# -----------------------------
# START GAME
# -----------------------------

if __name__ == "__main__":
    main()