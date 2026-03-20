# juego1vs1
 FIGHTING.io - Console RPG Game ⚔️

## Description 📌

This project is a simple turn-based fighting game developed in Python.
It allows players to battle either against the computer or against another player in a local match.

The game includes basic RPG mechanics such as:
	•	Random damage system 🎲
	•	Critical hits ⚡
	•	Healing with potions 🧪
	•	Special abilities 💥
	•	Turn-based combat 🔄

## Game Modes 🎮

The game offers two main modes:

1. Player vs Computer
	•	You control the Hero
	•	The computer controls the Enemy
	•	The enemy can attack or heal automatically

2. Player vs Player
	•	Two players take turns on the same device
	•	Each player chooses actions strategically

## Game Mechanics 🧠

Actions Available

Each player can choose between:
	•	Attack: Deals random damage
	•	Heal: Restores HP using potions
	•	Special Ability: High damage but chance to fail

Damage System
	•	Damage is randomly generated
	•	There is a 10% chance of critical hit, which doubles the damage

Health System
	•	Each player has a maximum HP
	•	Healing cannot exceed the maximum HP

Enemy Behavior
	•	If enemy HP is low, it heals
	•	Otherwise, it attacks

## Game Flow 🔄 
1.	The game starts with a main menu
2.	The player selects a game mode
3.	Players take turns:
	•	Choose an action
	•	Apply effects (damage, heal, etc.)
4.	The game checks for a winner after each turn
5.	The match ends when one player’s HP reaches 0

## Flowchart (Game Logic)

The following diagram represents the main logic of the game:
	•	Start
	•	Menu selection
	•	Game mode
	•	Player actions
	•	Victory check
	•	Loop until game ends
