#ImportingLibraries
import random

#DeterminingWinner

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!!!"
    else:
        return "Computer wins!!!"

def main():
    print("Welcome to Rock, Paper, Scissors game!")

    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        computer_choice = random.choice(['rock', 'paper', 'scissors'])

        print(f"Your choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
