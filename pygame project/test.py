import random
 
player_health = 100

boss_health = 200
 
def attack(target, damage):

    critical_hit = random.choice([True, False])

    if critical_hit:

        damage *= 2

        print("Critical Hit!")

    target -= damage

    return target
 
while player_health > 0 and boss_health > 0:

    player_action = input("Your turn: (attack/skip) ")

    if player_action == 'attack':

        boss_health = attack(boss_health, 15)

    if random.random() > 0.1:  # Boss has a 10% chance to miss

        player_health = attack(player_health, 20)

    print(f"Player health: {player_health}, Boss health: {boss_health}")
 

def boss_battle(player, boss):     
    print(f"A wild {boss.name} appears!")     
    while player.is_alive() and boss.is_alive():         
        print(f"\n{player.name}'s Health: {player.health}")         
        print(f"{boss.name}'s Health: {boss.health}")
 