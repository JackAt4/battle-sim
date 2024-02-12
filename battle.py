from os import system
from random import randint

class Actor:
    def __init__(self):
        self.hp = 10 # -- Health Points
        self.hpmax = self.hp
        self.ap = 2 # -- Action Points
        self.atk1 = 2 # -- Attack 1
        self.atk1ap = 0 # -- AP for Attack 1
        self.atk2 = 8 # -- Attack 2
        self.atk2ap = 3 # -- AP for Attack 2

player = Actor()
enemy = Actor()

def attack():
    is_blocked = False

    print(f" Your Health: {player.hp}\nEnemy Health: {enemy.hp}\n")
    print(f"Action Points - {player.ap}")

    print(f"1. Weak attack - (AP={player.atk1ap}, DMG<={player.atk1})")
    print(f"2. Strong attack - (AP={player.atk2ap}, DMG<={player.atk2})")
    print("3. Block (AP = 1)")
    print("4. Wait (AP +1)")
    action = input(">> ")

    if action == "1":
        print(f"You hit for {player.atk1} damage.")
        enemy.hp -= player.atk1
        player.ap -= player.atk1ap
    elif action == "2":
        damage = randint(player.atk2/2, player.atk2)
        print(f"You hit for {damage} damage.")
        enemy.hp -= damage
        player.ap -= player.atk2ap
    elif action == "3":
        chance = randint(1,10)
        if chance <= 80:
            print("You prepare to block.")
            is_blocked = True
        else:
            print("You lost your form and failed to block.")
            is_blocked = False
    return is_blocked

def enemy_attack(is_blocked):
    if not is_blocked:
        print(f"The enemy dealt {enemy.atk1} damage.")
        player.hp -= enemy.atk1
    else:
        print("The enemy attacked, but you deflected it")

def start():
    system("cls")

    while enemy.hp > 0 and player.hp > 0:
        blocked = attack()
        if enemy.hp <= 0:
            print("You win!")
        else:
            enemy_attack(blocked)
        if player.hp <= 0:
            print("You lose!")

    input("Press ENTER to Exit to Main Menu")