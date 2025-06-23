import random

rock = '''
  _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = ''' 
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]
choice_names = ["Rock", "Paper", "Scissors"]

# Scoreboard
total_wins = 0
total_losses = 0

print("Welcome to Rock, Paper, Scissors- Best of 3 mode!\n")

while True:
    user_score = 0
    computer_score = 0
    round_number = 0

    print("New match starting... First to 2 wins!\n")

    # Best of 3 loop
    while user_score < 2 and computer_score < 2:
        print(f"\n--- Round {round_number} ---")
        try:
            user_choice = int(input("Choose 0 for Rock, 1 for Paper, or 2 for Scissors: "))
            if user_choice not in [0, 1, 2]:
                print("Invalid input. Please enter 0, 1, or 2.")
                continue
        except ValueError:
            print("Please enter a number.")
            continue

        computer_choice = random.randint(0, 2)

        print(f"You chose {choice_names[user_choice]}")
        print(choices[user_choice])
        print(f"Computer chose {choice_names[computer_choice]}")
        print(choices[computer_choice])
        # Determine round winner
        if user_choice == computer_choice:
            print("It's a draw!")
        elif (user_choice == 0 and computer_choice == 2) or \
                (user_choice == 1 and computer_choice == 0) or \
                (user_choice == 2 and computer_choice == 1):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Score: You {user_score} - {computer_score} Computer")
        round_number += 1

    # Match result
    print("\nMatch Over!")
    if user_score > computer_score:
        print("You are the winner of the match!")
        total_wins += 1
    else:
        print("Computer wins the match. Better luck next time!")
        total_losses += 1

    print(f"Total Record: {total_wins} Wins - {total_losses} Losses")

    # Ask to play again
    play_again = input("\nDo you want to play another match? (Y/N): ").strip().lower()
    if play_again != 'y':
        print("\nThanks for playing! Final Scoreboard:")
        print(f"Wins: {total_wins}")
        print(f"Losses: {total_losses}")
        break
