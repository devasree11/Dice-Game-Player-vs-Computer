import random
def roll_dice():
    return random.randint(1, 6)
def display_roll(player, roll):
    print(f"{player} rolled: {roll}")
def single_player_game():
    user_score = 0
    computer_score = 0
    rounds = int(input("Enter number of rounds: "))
    for i in range(rounds):
        print(f"\n--- Round {i+1} ---")
        input("Press Enter to roll dice...")
        user_roll = roll_dice()
        comp_roll = roll_dice()
        display_roll("You", user_roll)
        display_roll("Computer", comp_roll)
        if user_roll > comp_roll:
            print("You win this round!")
            user_score += 1
        elif user_roll < comp_roll:
            print("Computer wins this round!")
            computer_score += 1
        else:
            print("It's a tie!")
    print("\n--- Final Result ---")
    print(f"Your Score: {user_score}")
    print(f"Computer Score: {computer_score}")
    if user_score > computer_score:
        print("🎉 You are the overall winner!")
    elif user_score < computer_score:
        print("💻 Computer wins overall!")
    else:
        print("🤝 Match Draw!")
def multiplayer_game():
    player1_score = 0
    player2_score = 0
    rounds = int(input("Enter number of rounds: "))
    for i in range(rounds):
        print(f"\n--- Round {i+1} ---")
        input("Player 1: Press Enter to roll...")
        roll1 = roll_dice()
        display_roll("Player 1", roll1)
        input("Player 2: Press Enter to roll...")
        roll2 = roll_dice()
        display_roll("Player 2", roll2)
        if roll1 > roll2:
            print("Player 1 wins this round!")
            player1_score += 1
        elif roll1 < roll2:
            print("Player 2 wins this round!")
            player2_score += 1
        else:
            print("It's a tie!")
    print("\n--- Final Result ---")
    print(f"Player 1 Score: {player1_score}")
    print(f"Player 2 Score: {player2_score}")
    if player1_score > player2_score:
        print("🏆 Player 1 is the winner!")
    elif player1_score < player2_score:
        print("🏆 Player 2 is the winner!")
    else:
        print("🤝 Match Draw!")
def main():
    while True:
        print("\n🎲 DICE GAME MENU")
        print("1. Single Player (vs Computer)")
        print("2. Multiplayer (2 Players)")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            single_player_game()
        elif choice == '2':
            multiplayer_game()
        elif choice == '3':
            print("Exiting game... Thank you!")
            break
        else:
            print("❌ Invalid choice! Please try again.")
main()
