import random
from fighter import Fighter
from ascii import display_title

display_title()

player_name = input("Enter your fighter's name: ").title()
player = Fighter(player_name, 20)

enemy_names = ["Blitz", "Venom", "Steel Jaw", "Mecha Rex", "Inferno", "Shadow Claw"]
enemy_name = random.choice(enemy_names)
opponent = Fighter(enemy_name, 20)

first_game = True
play_again = True

while play_again:
    # Reset HP at the start of every round
    player.hp = 100
    opponent.hp = 100

    if first_game:
        print(f"\n⚔️ {player.name} VS {opponent.name} - Prepare to FIGHT!\n")
        first_game = False
    else:
        print(f"\n⚔️ {player.name} VS {opponent.name} - REMATCH!\n")

    is_game_on = True

    while is_game_on:
        # --- PLAYER TURN ---
        choice = input("\nType 'roll' for a basic attack or 'risk' for a special move: ").lower()

        if choice == "roll":
            damage = random.randint(10, 20)
            player.attack(opponent, damage)

            if opponent.hp <= 0:
                print(f"\n{opponent.name} has been defeated! {player.name} wins!")
                is_game_on = False
                play_again_input = input("\nWould you like a rematch? (y/n): ").lower()

                if play_again_input != "y":
                    print("\nThanks for playing! 👋")
                    play_again = False
                    break

        elif choice == "risk":
            if random.random() < 0.5:
                damage = random.randint(30, 40)
                print("💥 Special move hits!")
                player.attack(opponent, damage)

                if opponent.hp <= 0:
                    print(f"\n{opponent.name} has been defeated! {player.name} wins!")
                    is_game_on = False
                    play_again_input = input("\nWould you like a rematch? (y/n): ").lower()

                    if play_again_input != "y":
                        print("\nThanks for playing! 👋")
                        play_again = False
                        break

            else:
                damage = random.randint(15, 25)
                print("⚠️ Special move backfired!")
                player.take_damage(damage)

                if player.hp <= 0:
                    print(f"\n{player_name} has been defeated by their own move! {opponent.name} wins!")
                    is_game_on = False
                    play_again_input = input("\nWould you like a rematch? (y/n): ").lower()

                    if play_again_input != "y":
                        print("\nThanks for playing! 👋")
                        play_again = False
                        break

        else:
            print("Invalid choice. You lose your turn!")

        # --- OPPONENT TURN ---
        print(f"\n{opponent.name}'s turn!")
        opponent_choice = random.choice(["roll", "risk"])

        if opponent_choice == "roll":
            damage = random.randint(10, 20)
            opponent.attack(player, damage)

            if player.hp <= 0:
                print(f"\n{player.name} has been defeated! {opponent.name} wins!")
                is_game_on = False
                play_again_input = input("\nWould you like a rematch? (y/n): ").lower()

                if play_again_input != "y":
                    print("\nThanks for playing! 👋")
                    play_again = False
                    break

        elif opponent_choice == "risk":
            if random.random() < 0.5:
                damage = random.randint(30, 40)
                print("🔥 Opponent's special move hits!")
                opponent.attack(player, damage)

                if player.hp <= 0:
                    print(f"\n{player.name} has been defeated! {opponent.name} wins!")
                    is_game_on = False
                    play_again_input = input("\nWould you like a rematch? (y/n): ").lower()

                    if play_again_input != "y":
                        print("\nThanks for playing! 👋")
                        play_again = False
                        break

            else:
                damage = random.randint(15, 25)
                print("💣 Opponent's special move backfired!")
                opponent.take_damage(damage)

                if opponent.hp <= 0:
                    print(f"\n{opponent.name} has been defeated by their own move! {player.name} wins!")
                    is_game_on = False
                    play_again_input = input("\nWould you like a rematch? (y/n): ").lower()

                    if play_again_input != "y":
                        print("\nThanks for playing! 👋")
                        play_again = False
                        break