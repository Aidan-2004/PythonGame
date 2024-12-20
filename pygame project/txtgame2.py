# Print a welcome message
print("Welcome to the Haunted Mansion!")
print("You are a distant family member of a rich millionaire who has just passed away, leaving this mansion to you.")
print("As the newfound owner, you decide to pay a visit to the mansion")
print("The house is dated, creaky and falling apart. You walk in the front door.")
print("Do you want to enter the living room or dining room?")

# Prompt user for a choice
room_choice = input("> ")

if(room_choice == "living room"):
    print("You enter the living room....")
    print("As you walk in you see a sleeping pitbull guarding some gold jewelry.")
    print("Do you want to steal the jewelry from the pitbull?")

    pitbull_choice = input("> ")

    if(pitbull_choice == "yes"):
        print("You attempt to steal the jewelry, but the pitbull wakes up and mauls you to death.")
        print("You are dead.")
    elif(pitbull_choice == "no"):
        print("You choose not to steal the dogs jewelry...")
        print("You turn around and leave the house safely.")
    else:
        print("Invalid choice. Please enter yes or no.")

elif(room_choice == "dining room"):
    print("You walk into the dining room...")
    print("As you walk in, you see a shiny box on a table.")
    print("Do you want to open the box?")

    box_choice = input("> ")

    if(box_choice == "yes"):
        print("You open the box and find a pile of bones!")
    elif(box_choice == "no"):
        print("You decide not to open the box.")
        print("As you turn to leave, you hear a cracking sound coming from the corner of the room...")
        print("A dark figure with glowing red eyes launches at you, knocking you unconcious....")
        print("You wake to find you are in your bed, It was all a dream.")
    else:
        print("Invalid choice. Please enter yes or no.")


else:
    print("Invalid choice. Please enter living room or dining room.")