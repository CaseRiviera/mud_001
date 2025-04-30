# refactored code
# -(*)-coding: utf-8-(*)-

import random
class Game: 
    def __init__(self):
        self.running = True

        def start_game(self):
            print("Welcome to the frst Multiplayer Dungeon!")
            print("Can I ask you one question?")
            print("Are you ready to build a new world?")
            print("If you are, please type 'yes' to continue.")
            response = input("Type 'yes' to continue: ").strip().lower()
            if response == 'yes':
                print("Great! Let's get started.")
                print("But first close your eyes and breathe")
            else:
                print("No problem! You can come back anytime, but you can also play the game.")
                print("Let's begin the adventure!")
                
                
# defining the game functions
    def talk (self):
        print("You hesistate to call out, unmsure who or what might be listening.")

    def look(self):
        print("You can make out figures moving to the left in the darkness and an ominous silence to the right.")
        print("In the distance you can hear the echoes of a womans sorrow as she sing a haunting melody.")

    def fight(self):\
        print("You encounter an enemy!")
        # Check enemy health and randomize cardinal position
``      enemy_health = random .randint(1, 100)
        enemy_position = random.choice([left, right, up, down])
    

        print("You are in a fight!")
        print("You can type 'attack' to attack the enemy.")
        print ("You can type 'defend' to defend yourself.")
        print("You can type 'run' to run away.")
        action = input("What do you want to do? ").strip().lower()
        if action == 'attack':
            print("You attack the enemy!)
             dmg =  random.stdint(0, 10)
             print(f"You hit the enemy for {dmg} damage!")

             # Check enemy health
                 
                print("You hit the enemy for 
        elif action == 'defend':