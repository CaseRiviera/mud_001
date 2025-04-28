# Our first MUD Adventure with AI
## Copyright (C) 2025 Rene Mauricio Lopez
## This program is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
## You should have received a copy of the GNU General Public License
## along with this program.  If not, see <http://www.gnu.org/licenses/>.
# -*- coding: utf-8 -*-

# A simple Multiplayer Dungeon text-based game
# @author: Rene Mauricio Lopez
# @email: renemlopez@proton.me
# @date: 2025-04-28
# @version: 0.1
# @license: GPLv3

import random

def start_game():
    print("Welcome to the first Multiplayer Dungeon!")
    print("Can I ask you one question?")
    print("Are you ready to build a new world?")
    print("If you are, please type 'yes' to continue.")
    response = input("Type 'yes' to continue: ").strip().lower()
    if response == 'yes':
        print("Great! Let's get started.")
    else:
        print("No problem! You can come back anytime, but you can also play the game.")
        print("Let's begin the adventure!")

# defining the game functions
def look():
    print("You can type 'look' to look around")

def fight():
    print("You are in a fight!")
    print("You can type 'attack' to attack the enemy.")
    print("You can type 'defend' to defend yourself.")
    print("You can type 'run' to run away.")
    action = input("What do you want to do? ").strip().lower()
    if action == 'attack':
        print("You attack the enemy and win!")
    elif action == 'defend':
        print("You defend yourself successfully!")
    elif action == 'run':
        # randomly determine if the player escapes
        if random.choice([True, False]):
            print("You run away successfully!")
        else:
            print("You couldn't escape! The enemy attacks you!")
            # simulate enemy attack
            if random.choice([True, False]):
                print("You are injured!")
            else:
        print("You run away safely!")
    else:
        print("Invalid action. The enemy attacks you!")

def move():
    print("You are moving!")
    print("You can type 'left' to move left.")
    print("You can type 'right' to move right.")
    print("You can type 'forward' to move forward.")
    print("You can type 'backward' to move backward.")
    direction = input("Which direction do you want to move? ").strip().lower()
    if direction in ['left', 'right', 'forward', 'backward']:
        print(f"You move {direction}.")
    else:
        print("Invalid direction.")

if __name__ == "__main__":
    start_game()

    # Main game loop
    while True:
        print("You awaken in an open glen surrounded by old oak trees, rays of sun wash over your body. Their warmth heals the wounds of an old world.")
        print("Half-rising and holding yourself up, you begin to feel the energy the light is imbibing your skin with.")
        print("Recalling the sins of the past and now sitting in the grass in what could only be considered a...video game?")
        print("You can make out figures moving to the left deeper in the trees and hear the sounds of a solitary crow in the distance.")
        print("The singing of the birds has reached a crescendo, the wind rises and your hair...or lack of it, is set ablaze.")
        print("You can do anything you want, but you have to be careful.")
        print("You can type 'help' to see the available commands.")
        print("You can type 'exit' to quit the game.")
        command = input("What do you want to do? ").strip().lower()

        if command == 'help':
            print("Available commands: help, exit, look, move, talk, fight")
        elif command == 'exit':
            print("Thanks for playing! Goodbye!")
            break
        elif command == 'look':
            print("You can make out figures moving to the left in the darkness and an ominous silence to the right.")
        elif command == 'move':
            move()
        elif command == 'talk':
            print("You hesitate to call out, unsure who or what might be listening.")
        elif command == 'fight':
            fight()
        else:
            print("Unknown command. Type 'help' to see the available commands or 'exit' to quit the game.")