# Blackjack Game in Python

This is a simple console-based Blackjack game made using Python. I created this project to practice basic Python concepts and understand how they can be used together to make a small game.

## About the Game

Blackjack is a card game where the goal is to get a hand value as close to 21 as possible without going over 21.

In this game, the player plays against the dealer.

### Card Values

* Cards from 2 to 10 have their face value.
* J, Q and K are worth 10.
* A can be worth 1 or 11 depending on the hand.

## Features

* Creates a standard 52-card deck
* Randomly shuffles the cards
* Deals cards to the player and dealer
* Player can choose Hit or Stand
* Automatically calculates the value of the hand
* Handles Aces as 1 or 11
* Detects Blackjack
* Detects when the player or dealer busts
* Dealer automatically draws cards until reaching 17
* Shows whether the player wins, loses or draws
* Includes a virtual betting system
* Starts with a balance of $1000
* Allows the player to play multiple rounds
* Handles invalid user input

## Technologies Used

* Python 3
* Random module

No external libraries are required.

## Project Structure

```text
Blackjack/
│
├── blackjack.py
└── README.md
```

## How to Run

First, clone the repository:

```bash
git clone https://github.com/yourusername/blackjack-python.git
```

Go into the project folder:

```bash
cd blackjack-python
```

Run the Python file:

```bash
python blackjack.py
```

If `python` does not work, you can try:

```bash
python3 blackjack.py
```

## How to Play

The game starts with a balance of $1000.

The player first enters the amount they want to bet.

Example:

```text
Your balance: $1000
Enter your bet: $50
```

The player and dealer are then dealt two cards.

The player can choose between:

```text
Hit
Stand
```

### Hit

Choosing Hit gives the player another card.

### Stand

Choosing Stand ends the player's turn and the dealer starts playing.

The dealer keeps drawing cards until the hand value is at least 17.

## Winning

The player wins when:

* Their hand is closer to 21 than the dealer's hand.
* The dealer goes over 21.
* The player gets Blackjack and the dealer does not.

The player loses when:

* Their hand goes over 21.
* The dealer has a higher hand value.
* The dealer gets Blackjack.

If both the player and dealer have the same value, the round is a draw.

## Betting

The game uses virtual money.

The starting balance is:

```text
$1000
```

The bet is added to the balance when the player wins and deducted when the player loses.

The game does not use real money.

## Python Concepts Used

While making this project, I used several basic Python concepts, including:

* Lists
* Tuples
* Functions
* For loops
* While loops
* If/elif/else statements
* User input
* Exception handling
* Random numbers
* Variables and arithmetic operations

## Future Improvements

Some things I would like to add to this project in the future are:

* A graphical user interface using Tkinter
* Playing card images
* Better game design
* Sound effects
* Card animations
* Player statistics
* Win and loss tracking
* A better betting system

## Author

Tanya
