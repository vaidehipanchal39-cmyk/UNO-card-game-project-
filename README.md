# UNO-card-game-project-
Project Title
UNO Card Game – Player vs Computer
📖 Overview of the Project
This project is a simple UNO card game developed using Python. The game allows a human player to play UNO against a computer opponent through the command-line/console.
The program creates and shuffles a standard UNO-style deck, deals cards to the player and computer, checks whether cards can be played, handles special cards such as Skip, Reverse, Draw 2, Wild, and Wild Draw 4, and determines the winner.
The project demonstrates the use of Python functions, lists, dictionaries, loops, conditional statements, user input, and the random module.
⭐ Features
Automatically creates and shuffles an UNO deck.
Supports one human player and one computer player.
Deals 7 cards to each player.
Uses colors for red, green, blue, and yellow cards.
Supports Skip, Reverse, Draw 2, Wild, and Wild Draw 4.
Checks whether a card is a valid move.
Allows the player to draw a card.
Computer automatically selects a playable card.
Reuses and shuffles the discard pile when the deck becomes low.
Automatically checks the winner.
Runs in the Python console/terminal.
🛠️ Technologies / Tools Used
Technology / Tool
Purpose
Python
Main programming language
Random Module
Shuffling the UNO deck
ANSI Escape Codes
Terminal card colors
Lists
Cards, colors, values, and hands
Dictionaries
Player hands and color codes
Functions
Organizing game logic
Console/Terminal
Running the game
📂 Project Structure
UNO-Card-Game/
├── uno_game.py
└── README.md
⚙️ Steps to Install & Run the Project
Step 1: Install Python
Check whether Python is installed:
python --version
or:
python3 --version
Step 2: Save the Python Code
Save the game code as:
uno_game.py
Step 3: Open Terminal / Command Prompt
Navigate to the project folder:
cd UNO-Card-Game
Step 4: Run the Game
python uno_game.py
or:
python3 uno_game.py
🎮 How to Play
The game displays the top card and your current hand. Enter a card number to play a card, or enter D to draw.
Example:
Options: Type a card number to play, or type 'D' to draw.
Your choice is: 2
To draw:
D
🃏 Card Rules Implemented
Number Cards
A number card can be played when its color or value matches the top card.
Skip Card
The player gets another turn after playing Skip.
Reverse Card
In this two-player version, Reverse gives the same player another turn.
Draw 2 Card
The opponent draws two cards and the current player gets another turn.
Wild Card
A Wild card can be played regardless of the top card's color.
Wild Draw 4
A Wild Draw 4 can be played regardless of the top card's color in this implementation.
🤖 Computer Player
The computer searches its hand for a valid card. If none is available, it draws a card. If the drawn card is playable, it automatically plays it.
🏆 Winning Condition
If the player's hand becomes empty:
Congratulations! You won the game!
If the computer's hand becomes empty:
Game over! The computer won the game.
🧪 Instructions for Testing
Test 1 – Game Starts
Run the program. Verify that a deck is created, shuffled, 7 cards are dealt to each player, and a starting card is displayed.
Test 2 – Valid Card
Play a card matching the top card's color or value. The card should be accepted.
Test 3 – Invalid Card
Play a card matching neither color nor value. The program should show:
Invalid card selection! It doesn't match the top card.
Test 4 – Draw Card
Enter D. A card should be drawn from the deck.
Test 5 – Wild Card
Play Wild or Wild Draw 4. It should be accepted regardless of the top card's color.
Test 6 – Draw 2
Play Draw 2. The opponent should receive two cards.
Test 7 – Winning
Continue until one player's hand is empty. The winner message should appear and the game should stop.
🖥️ Sample Output
=========================
*************************
LET'S START THE GAME!
*************************
=========================

Starting card on the table: red5

-------------------------
Top card on table: red5
Computer has 7 cards left.

Your current hand:
1. blue5
2. green7
3. yellow2
4. redSkip
5. blue9
6. Wild
7. green3

Options: Type a card number to play, or type 'D' to draw.

Your choice is: 1

You played: blue5
🔧 Important Code Note
The current code creates the player hand as:
hands = {"player": [], "Computer": []}
So all player-hand references should consistently use hands["player"], not hands["You"].
For example:
hands["player"].append(draw)
chosenCard = hands["player"][idx]
hands["player"].remove(draw)
This correction prevents a KeyError when running the game.
 Future Improvements
Graphical user interface (GUI)
Clickable cards
Sound effects
Score tracking
Multiplayer mode
Improved computer strategy
Proper Wild Card color selection
Game statistics
Online multiplayer
Restart/new-game button
👩‍💻 Conclusion
This UNO Card Game project demonstrates fundamental Python programming concepts through an interactive Player-vs-Computer game. It uses functions, loops, lists, dictionaries, conditional statements, randomization, user input, and exception handling.
The project can be further developed into a graphical or multiplayer UNO application.
