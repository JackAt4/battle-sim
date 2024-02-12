from os import system
from random import randint

class Actor:
    def __init__(self):
        self.hp = 10 # -- Health Points
        self.hpmax = self.hp
        self.ap = 2 # -- Action Points
        self.atk1 = 2 # -- Attack 1
        self.atk1ap = 1 # -- AP for Attack 1
        self.atk2 = 8 # -- Attack 2
        self.atk2ap = 3 # -- AP for Attack 2

player = Actor()
enemy = Actor()

def attack():
    is_blocked = False

    print(f"\n Your Health: {player.hp}\nEnemy Health: {enemy.hp}\n")
    print(f"Action Points - {player.ap}")

    print(f"1. Weak attack - (AP={player.atk1ap}, DMG<={player.atk1})")
    print(f"2. Strong attack - (AP={player.atk2ap}, DMG<={player.atk2})")
    print("3. Block (AP=0)")
    print("4. Wait (AP +2)")
    action = input(">> ")

    system("cls")
    if action == "1" and player.ap >= player.atk1ap:
        print(f"Your Turn: You slashed at the enemy for {player.atk1} damage.")
        enemy.hp -= player.atk1
        player.ap -= player.atk1ap
    elif action == "2" and player.ap >= player.atk2ap:
        damage = randint(player.atk2/2, player.atk2)
        print(f"Your Turn: You slashed the enemy for {damage} damage.")
        enemy.hp -= damage
        player.ap -= player.atk2ap
    elif action == "3":
        chance = randint(1,10)
        if chance <= 8:
            print("Your Turn: You prepare to block their next attack.")
            is_blocked = True
        else:
            print("Your Turn: You lost your balance and failed to block.")
            is_blocked = False
    elif action == "4":
        player.ap += 2
    
    return is_blocked

def enemy_attack(is_blocked):
    if not is_blocked and enemy.hp > 0 and enemy.ap > 0:
        print(f"Their Turn: The enemy dealt {enemy.atk1} damage.")
        player.hp -= enemy.atk1
        enemy.ap -= enemy.atk1ap
    elif enemy.hp <= 0:
        print("Their Turn: The enemy was about to attack, but you killed it before it could hurt you")
    elif enemy.ap <= 0:
        print("Their Turn: The enemy took a moment to catch their breath")
        enemy.ap += 2
    else:
        print("Their Turn: The enemy attacked, but you deflect it")

def start():
    system("cls")

    while enemy.hp > 0:
        if player.hp > 0:
            enemy_attack(attack()) # The player attack returns if blocking the enemy
        if player.hp <= 0:
            break
    
    if enemy.hp <= 0:
        print("\nThe enemy falls and lies motionless\n")
    elif player.hp <= 0:
        print("\nYour world goes black\n")

    input("Press ENTER to Exit to Main Menu")