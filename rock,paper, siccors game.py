import random 

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Tie"
    elif (player_choice == 'r' and computer_choice == 's') or \
         (player_choice == 'p' and computer_choice == 'r') or \
         (player_choice == 's' and computer_choice == 'p'):
        return "You win"
    else:
        return "You lose"

print("Welcome to the Rock, Paper, Scissors game!")

while True:
    choices = ['r', 'p', 's']
    player_choice = input("Choose from (rock, paper, scissors): ").lower()
    
    # Validate player's choice
    if player_choice not in choices:
        print("Invalid choice. Please choose again.")
        continue
    
    computer_choice = random.choice(choices)
    print("Computer choice:", computer_choice)
    print("Your choice:", player_choice)
    
    result = determine_winner(player_choice, computer_choice)
    print("Result:", result)
    
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thank you for playing!")
        break
