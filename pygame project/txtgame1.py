import os

# Display starting menu
def prompt():
    print("\t\t\tWelcome to the dungeon\n\n\
          You must collect all six items before fighting the boss. \n\n\
          \tMoves:'go {direction}' (travel north, south, east, west)\n\
          \t'get {item}' (add a nearby item to inventory)\n\
          \t'exit' to exit the game\n\n ")
    
    input("Press any key to continue...")

# Clears screen
def clear():
          os.system('cls' if os.name == 'nt' else 'clear')

# Map
rooms = {
       'Liminal Space': {'North': 'Mirror Maze', 'South': 'Bat Cavern', 'East': 'Bazaar', 'Info': 'An empty space filled with nothing, not even shadows.'},
       'Mirror Maze': {'South': 'Liminal Space', 'Item': 'Crystal', 'Info': 'Some ancient madmans magnum opus of mirrors and confusion twists off into the shadows. Each distorted pathway a haze of relected realities.'},
       'Bat Cavern': {'North': 'Liminal Space', 'East': 'Volcano', 'Item': 'Staff', 'Info': 'A dark and sullen place permeated with the smell of fresh guano. The occasional warning shrieks out of the darkness writhing above you.'},
       'Bazaar': {'West': 'Liminal Space', 'North': 'Meat Locker', 'East': 'Dojo', 'Item': 'Altoids', 'Info': 'A once bustling place now lifeless and silent. The discarded belongings of its ghostly inhabitants the only epitath of the society that once lived here.'},
       'Meat Locker': {'South': 'Bazaar', 'East': 'Quicksand Pit', 'Item': 'Fig', 'Info': 'Nothing but the smell of putrid meat inhabits this place. The walls and floor smeared with bloodstains almost black with age.'},
       'Quicksand Pit': {'West': 'Meat Locker', 'Item': 'Robe', 'Info': 'The danger of this place sets you on edge with every breath. The thought skips through your mind that each step may be the one to pull you down to meet a silent end below.'},
       'Volcano': {'West': 'Bat Cavern', 'Item': 'Elderberry', 'Info': 'The heat emanating from the volcano blurs your vision. You raise your hand to shield your eyes letting you barely make out your surroundings.'},
       'Dojo': {'West': 'Bazaar', 'Boss': 'Shadow Man', 'Info': 'You  have reached the dojo where you face off against the master. Will you survive?'}
        }

# List of vowels
vowels = ['a', 'e', 'i', 'o', 'u']

# Player starting HP (Hit Points)
player_HP = 10

# Boss starting HP
boss_hp = 10

# List to track inventory
inventory = []

# Tracks current room
current_room = "Liminal Space"

# Result of last move
msg = ""

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

    # Boss encounter
    if "Boss" in rooms[current_room].keys():
                
        # Lose condition
        if len(inventory) < 6:
            print(f"You lost a fight with {rooms[current_room]['Boss']} and died.....")
            break

        # Win condition
        else:
            print(f"You beat {rooms[current_room]['Boss']}!")
            break

    # Accept players move as input
    user_input = input("What do you do?:\n")

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
        