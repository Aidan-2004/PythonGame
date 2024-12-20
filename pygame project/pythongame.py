# IMPORTS
from random import randint
from os import system, name
from time import sleep

ascii_art_congrats = """888            
                                               888            
                                               888            
 .d8888b .d88b. 88888b.  .d88b. 888d888 8888b. 888888.d8888b  
d88P"   d88""88b888 "88bd88P"88b888P"      "88b888   88K      
888     888  888888  888888  888888    .d888888888   "Y8888b. 
Y88b.   Y88..88P888  888Y88b 888888    888  888Y88b.      X88 
 "Y8888P "Y88P" 888  888 "Y88888888    "Y888888 "Y888 88888P' 
                             888                              
                        Y8b d88P                              
                         "Y88P"                               
"""

# FUNCTIONS

# Display starting menu
def prompt():
    print("\t\t\tWelcome to the dungeon\n\n\
        \tYou must collect all the items before fighting the boss. \n\n\
        \tMoves:'go {direction}' (travel north, south, east, west)\n\
        \t'get {item}' (add a nearby item to inventory)\n\
        \t'exit' to exit the game\n\n ")
    input("Press any key to continue...")

# Clears screen in any operating system
def clear():
    system('cls' if name == 'nt' else 'clear')

def player_wins():
    print("As the rumbling comes to a stand still, the creature transforms in front of your eyes. The intertwined vines and branches unclench from their roots as the rock and sediment soften. A bright green burst of light surrounds the area. An Elven woman emerges from the once mutated creature and stands before you, teary eyed and exhausted. Elven Woman: “Y-You did it…! Thank you!” Elven Woman: “It seems you have been searching for me as I have been searching for a way out of this treacherous curse. Oh? That sword…of course…of course that was the key.” *You look at the sword and is now drained from all of its colour and left with an obsidian sheen* Elven Woman: “It was emerald wasn’t it? The curse that was linked to me was embedded by the material of that very sword…you defeated me breaking the curse's bond! Any-hoo! You must be wanting to know who I am and why I know this. I’m the Witch of the Earth.” *Your eyes widen and you explain how you need to get home* Witch of the Earth: “I know what your heart desires, fear not, I will grant it true.” The Witch closes her eyes and a white light penetrates the wall behind you, creating a new door.Witch of the Earth: “Your home awaits, adventurer…”")
    print(ascii_art_congrats)
    quit()
    
def player_loses():
    print(f"You have been killed!")
    print(f"Game Over!")
    quit()

def trap_encounter():
    global rooms, vowels, player_HP, boss_hp, inventory, current_room, msg, previous_room, dice_roll
    if "Trap" in rooms[current_room].keys():
        print(f"You have encountered a trap. You must roll to save yourself.")
        user_input = input("What do you do?(roll):\n").lower()
        user_input_unclear = True
        while user_input_unclear:
            print(user_input)
            print(user_input.find("roll"))
            if user_input.find("roll") != -1: # Roll!
                user_input_unclear = False
                if dice_roll <= 4: # condition
                    print("After falling for some time you end up in a room. A sudden gush of frozen air collides you with a burning sensation of hot air. The convergence of hot and cold rips into your skin and throws you swiftly into a wall full of razor-sharp spikes, meeting your untimely death......")
                    player_loses()
                else:
                    print("You avoided the trap, this time...")

            else:
                print("Your decision not to roll has lead to your demise...")
                # user_input_unclear = True
                player_loses()

def boss_encounter():
    global rooms, vowels, player_HP, boss_hp, inventory, current_room, msg, previous_room, back_room
    if "Boss" in rooms[current_room].keys():
        boss_name = rooms[current_room]["Boss"]
        print(f"You have entered a room with the {boss_name}. If you have your full inventory you may fight the boss to win the game. If you do not have your full inventory you will loose and die!")
        user_input = input("What do you do?(fight or go back):\n").lower()
        user_input_unclear = True
        while user_input_unclear:
        #     print(user_input)
        #     print(user_input.find("fight"))
            if user_input.find("fight") != -1: # Fight!
                user_input_unclear = False
                if len(inventory) < 4: # condition
                    print(f"You lost a fight with {boss_name} and died.....")
                    player_loses()
                else: # Fight condition
                    while player_HP > 0 and boss_hp > 0:
                        print(f"You hit {boss_name}")
                        boss_hp = boss_hp - randint(5,20)
                        print(f"Their health is now {boss_hp}")
                        print(f"{boss_name} hits you")
                        player_HP = player_HP - randint(2,14)
                        print(f"Your health is now {player_HP}")
                        print(f"You pause for a moment... before lunging again")
                        sleep(1.5)
                        
                    if player_HP <= 0:
                        player_loses()
                    else:
                        player_wins()
            if user_input.find("back") != -1: # Go Back
                print("line 86")
                user_input_unclear = False
                current_room = back_room
                break
            else:
                print("I do not understand your input choose fight or back")
                user_input_unclear = True
                break
                
def item_indicator():
    global rooms, vowels, player_HP, boss_hp, inventory, current_room, msg, previous_room
    if "Item" in rooms[current_room].keys():
        nearby_item = rooms[current_room]["Item"]
        if nearby_item not in inventory:
        # Plural
            if nearby_item[-1] == 's':
                print(f"You see {nearby_item}")
        # Singular starts with vowel
            elif nearby_item[0] in vowels:
                print(f"you see an {nearby_item}")
                # Singular starts with consanant
            else:
                print(f"You see a {nearby_item}")


# GLOBAL VARIABLES

# Map
rooms = {
        'Cell 2':
            {'South': 'Guard room',
                'Info': 'A coldness trails up your spine and startles you awake. You lack the knowledge of how you ended up here but you are aware that this is unfamiliar territory and need to escape. Glancing at the surroundings, half of the room is frozen and half of the room is singed from fire. Your path is blocked by a heavy metal door, it is locked. You notice a dim light from an opening in the wall that is bolted over with 3 rusted metal bars. A slender figure is slumped in the corner of the room, the darkness shrouds their expression but you sense that they are surprised by your presence.'},
        'Guard room':
            {'South': 'Stairway', 'East': 'Cell 3', 'North': 'Cell 2', 'West': 'Cell 1', 'Item': 'Torch',
                'Info': 'You come across a room which is dimly lit by two torches either side of a doorway. A table and 2 chairs sit in the middle of the room with empty cups lay on top next to an unfinished game of chess. A drunken Dragonborn Guard sits in one of the chairs, seemingly unaware of your presence. You need to get to the doorway to progress.'},
        'Cell 1':
            {'East': 'Guard room',
                'Info': 'Another cell, just like yours, comes into view. The room is ice cold, the atmosphere has produced almost snow-like weather within the room. You can feel your temperature drop.'},
        'Cell 3':
            {'West': 'Guard room','Item': 'Compass',
                'Info': 'You come across a weathered cell with a heavy metal door pried from its hinges. You feel an immense feeling of unease as you step into the room. The floor is scattered with clumps of straw and moss that have intertwined with each other. A shackled skeleton lies in the corner with remains of cloth clinging to the bones. Within the skeleton’s fragile grip, a round object sits.'},
        'Stairway':
            {'South': 'Corridor', 'North': 'Guard room', 'East': 'Dungeons',
                'Info': 'You exit the guard room onto a stairway. You see a layer of ice glistening from your torch, the chill in the room sends a shiver down your spine. To proceed, you must get to the doorway at the top of the stairs. You see a passage to the east.'},
        'Dungeons':
            {'West': 'Stairway', 'Trap': 'true',
                'Info': 'After falling through the trap door you end up in a dark dungeon its filled with devices that you cannot understand its uses for. Netting is strung from the cealing with rough stone and metallic sheets on the walls. All you know is a foul stench of dried blood and other fluids lingers in the air. Which leads to you only feel a sense of dread knowing that your adventure might have take a turn for the worse.'},
        'Corridor':
            {'North': 'Stairway', 'East': 'Storeroom', 'South': 'Armoury',
                'Info': 'You come to a long corridor. Your eyes narrow as the darkness swallows the other end. As the darkness surrounds you, you notice a soot-like material saturating the floor and walls. The material, although it was almost powder, resembled flesh - the thought bewildered you. You notice a clean, untouched door to the east that shimmered from ice.'},
        'Storeroom':
            {'West': 'Corridor', 'Item': 'Key',
                'Info': 'You stand in front of an ice glimmering door and turn the metal knob that pierced your hand with a bitter cold. The room was no bigger than 2 meters wide and 3 meters long. It was stacked neatly with barrels and shelving, suspiciously untouched despite the turmoil just outside the room. It was brightly lit from candles, dripping with wax, scattered throughout which gave you a sense of safety from the darkness behind you.'},
        'Armoury':
            {'North': 'Corridor', 'East': 'Hallway', 'Item': 'Sword',
                'Info': 'The heat emanating from the volcano blurs your vision. You raise your hand to shield your eyes letting you barely make out your surroundings.'},
        'Hallway':
            {'West': 'Armoury', 'East': 'Throne room',
                'Info': 'You  have reached the dojo where you face off against the master. Will you survive?'},
        'Throne room':
            {'West': 'Hallway', 'Boss': 'Evil Witch',
                'Info': 'Letting the huge doors slam shut behind you, you enter a grand space which resembles a throne room. The room is vast, with a high sculpted ceiling and pillars carved from bone. An abnormal sized throne sits on the back wall towering to almost touch the highest points of the ceiling. The room is swallowed by forest, vines intertwining through rock and wood and humongous trees forcing their roots through the structure; the foundation of the room has been replaced by growing vegetation. A rumble shifts you off your feet as the room starts to crumble around you. Rising from the floor, a mutated amalgamation of rock, earth and intertwined trees roars from its slumber. The creature glows, a similar glow as the emerald sword, which pulsates throughout its body. Without hesitation the mutation locks onto your position.'},
        # 'Exit':
        #     {'South': 'Throne room', 'Info': 'As you leave the dungeon you look back to behold a withered castle, scarred with the passing of ages. The sun shines high in the sky and you get a sense of excitement as you realise you survived. Now you set forth to carve out your new life in this new world.'}
        }

# List of vowels
vowels = ['a', 'e', 'i', 'o', 'u']

# Player starting HP (Hit Points)
player_HP = 60

# Boss starting HP
boss_hp = 50

# List to track inventory
inventory = []

# Tracks current room
current_room = "Cell 2"
previous_room = "Cell 2"
back_room = "Hallway"

# Result of last move
msg = ""

# Dice roll
dice_roll = randint(1, 11)

# GAMEPLAY

clear()
prompt()

# Gameplay loop
while True:
    clear()

    # Display msg
    print(msg)

    # Room description
    room_info = rooms[current_room]["Info"]

    # Display info player
    print(f"You are in the {current_room}\n{room_info}\n{'-' * 27}\n HP : {player_HP}\n Inventory : {inventory}\n{'-' * 27}")

    # Item indicator
    item_indicator()
    
    # Boss encounter
    boss_encounter()

    # Room encounter
    trap_encounter()
 
    # Accept players move as input
    user_input = input("What do you do now?:\n")
 
    # Splits move into words
    next_move = user_input.split(' ')
 
    # First word is action
    action = next_move[0].title()
 
    if len(next_move) > 1:
        item = next_move[1:]
        direction = next_move[1].title()
        item = ' '.join(item).title()
 
    # Moving between rooms
    if action == "Go":
                 
        try:
            current_room = rooms[current_room][direction]
            msg = f"You travel {direction}."
 
        except:
            msg = f"You cant go that way."
                     
    # Picking up items
    elif action == "Get":        
        try:
            if item == rooms[current_room]["Item"]:
                if item not in inventory:
                        inventory.append(rooms[current_room]["Item"])
                        msg = f"{item} retrieved"
                else:
                        msg = f"You already have the {item}."
            else:
                    msg = f"Cant find {item}"
        except:
                msg = f"Cant find {item}"
    # Exit game
    elif action == "Exit":
        break
    # Any other commands invalid
    else:
        msg = "Invalid command"

      