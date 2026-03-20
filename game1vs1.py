import random

def generate_damage(minimum, maximum): #daño aleatorio
    damage = random.randint(minimum, maximum)

    if random.random() < 0.1:
        print("CRITICAL HIT!")
        damage *= 2

    return damage

def show_status(name1, hp1, max1, name2, hp2, max2,potions, potions2): #estado
    def health_bar(hp, max_hp):
        #barra_salud
        total = 10
        filled = int((hp / max_hp) * total)
        empty = total - filled             #vacio
        return "[" + "❤️" * filled + "-" * empty + "]"
    
    
    
    print("____________________________________________\n")
    print("*** STATUS ***\n")
    print(f"{name1}: {hp1} HP {health_bar(hp1, max1)}  potions: {potions}")
    print(f"{name2}: {hp2} HP {health_bar(hp2, max2)}  potions: {potions2}")
    print("____________________________________________\n")
    

def player_turn(name, opponent_hp, player_hp, potions, max_hp): #vida
    while True:
        print(f"\n{name}'s turn:\n1. Attack \n2. Heal \n3. Special Ability\n")

        option = input("Choose an action -> ") #opcion de ataque

        if option == "1":
            damage = generate_damage(10, 25)
            opponent_hp -= damage
            print(f"\n*** {name} deals {damage} damage! ***\n")
            print(f"-> Enemy HP is now: {opponent_hp}")
            break

        elif option == "2":
            if potions > 0:
                player_hp += 20
                if player_hp > max_hp:
                    player_hp = max_hp
                potions -= 1
                print(f"\n{name} heals 20 HP!")
                break
            else:
                print("No potions left!")

        elif option == "3":
            if random.random() < 0.5:
                damage = generate_damage(30, 50)
                opponent_hp -= damage
                print(f"\n- Special ability! {name} deals {damage} damage!")
                print(f"\n-> Enemy HP is now: {opponent_hp}\n")
            else:
                print("\n- Special ability missed!")
            break

        else:
            print("** Invalid option. **")

    return opponent_hp, player_hp, potions


def enemy_turn(player_hp, enemy_hp): #demage
    if enemy_hp <= 24:
        print("\n-> Enemy heals...")
        enemy_hp += 15
        if enemy_hp > 120:
            enemy_hp = 120
        print(f"\n-> Enemy HP is now: {enemy_hp}")
    else:
        damage = generate_damage(15, 20)
        player_hp -= damage
        print(f"\n- Enemy deals {damage} damage!")
        print(f"\n** Your HP is now: {player_hp} **")

    return player_hp, enemy_hp


def check_winner(hp1, hp2, name1, name2): #quien gano 
    if hp1 <= 0:
        print(f"{name1} has been defeated!")
        print(f"\n*** {name2} WINS! ***\n")
        return True
    elif hp2 <= 0:
        print(f"{name2} has been defeated!")
        print(f"\n*** {name1} WINS! ***\n")
        return True
    return False


def vs_computer(): #vs el computador
    hp_player = 100
    hp_enemy = 120
    potions = 3
    potions2 = 3
    while True:
        show_status("Hero", hp_player, 100, "Enemy", hp_enemy, 120, potions,potions2)

        hp_enemy, hp_player, potions = player_turn("Hero", hp_enemy, hp_player, potions, 100)

        if check_winner(hp_player, hp_enemy, "Hero", "Enemy"):
            break

        hp_player, hp_enemy = enemy_turn(hp_player, hp_enemy)

        if check_winner(hp_player, hp_enemy, "Hero", "Enemy"):
            break


def player_vs_player(): #juagdor contra jugador
    hp1 = 100
    hp2 = 100
    potions1 = 3
    potions2 = 3

    print("\nPlayer 1: Choose your role")
    print("1. Hero")
    print("2. Enemy")
    choice = input("Option: ")

    if choice == "1":
        name1 = "Hero"
        name2 = "Enemy"
    else:
        name1 = "Enemy"
        name2 = "Hero"

    while True:
        show_status(name1, hp1, 100, name2, hp2, 100, potions1,potions2)

        hp2, hp1, potions1 = player_turn(name1, hp2, hp1, potions1, 100)

        if check_winner(hp1, hp2, name1, name2):
            break

        hp1, hp2, potions2 = player_turn(name2, hp1, hp2, potions2, 100)

        if check_winner(hp1, hp2, name1, name2):
            break


def main(): #menu
    print("\n*** FIGHTING.io ***\n")

    while True:
                #escoge el modo de juego
        print('-> Choose a game mode: ')
        print("1. Play vs Computer")
        print("2. 2 Players Mode")
        print("3. Exit")

        option = input("Choose an option: ")

        if option == "1":
            vs_computer()
        elif option == "2":
            player_vs_player()
        elif option == "3":
            print("\n*** Goodbye! ***")
            break
        else:
            print("\nInvalid option.\n")

main()
