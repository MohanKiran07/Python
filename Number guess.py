import random

def compare_numbers(player_guess, computer_guess):
    if player_guess == computer_guess:
        return "Congratulations! You guessed the number correctly."
    else:
        return "Sorry, your guess was incorrect."

while True:
    player_input = input("Guess a number between 1 to 5: ")
    computer_choices = ['1', '2', '3', '4', '5']
    computer_guess = random.choice(computer_choices)
    
    result_message = compare_numbers(player_input, computer_guess)
    print(result_message)

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != 'yes':
        print("Thanks for playing!")
        break
