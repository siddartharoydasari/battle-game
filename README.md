# battle-game
Two-Player Battle Game
# Overview
This is a simple two-player battle game where two players take turns to attack or defend. The goal of the game is to deplete the opponent’s HP (Health Points) to 0. Players can choose between attacking or defending each turn. If one player is defending, their opponent's attack will deal less damage.

The game runs in a terminal/command-line interface and uses random values to simulate the damage and outcomes of attacks.

# Features
Two players (Player 1 and Player 2) take turns to either attack or defend.
Each player has 100 HP at the start of the game.
Attack damage is randomly generated between 10 to 20 points.
If a player defends, the incoming attack damage is halved.
The game ends when one player's HP reaches zero, and the other player wins.
# How to Play
Clone or download the repository.

Open a terminal or command-line interface.

Run the Python script to start the game.

bash
Copy
python game.py
# During the game, each player will be prompted to either:

Attack: Inflict random damage to the opponent.
Defend: Halve the damage taken from the opponent's next attack.
The game will continue until one player's HP is reduced to zero, and the winner is announced.

# Example
Here’s an example of what playing the game might look like in the terminal:


Game Starting...

------Turn Start-------
Player 1 HP: 100
Player 2 HP: 100
Player 1's Turn
Choose attack or defend: attack
Generating attack.....💥
Player 1 has attacked Player 2 for 15 damage!⚔️

------Turn Start-------
Player 1 HP: 100
Player 2 HP: 85
Player 2's Turn
Choose attack or defend: defend
Player 2 is defending this turn.

------Turn Start-------
Player 1 HP: 100
Player 2 HP: 85
Player 1's Turn
Choose attack or defend: attack
Generating attack.....💥
Player 1 has attacked Player 2 for 10 damage!⚔️

...and so on until one player wins!
# Requirements
Python 3.x
No external libraries are required (all dependencies are built-in to Python).
# How to Contribute
Fork the repository.
Create a new branch.
Make your changes.
Submit a pull request.
