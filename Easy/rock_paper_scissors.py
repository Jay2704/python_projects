import random  # Import the random module to generate random choices for the computer

def play():
    """
    Function to handle one round of the Rock, Paper, Scissors game.
    """
    # Prompt the user to enter their choice
    user_turn = input("Enter\n"
                      "1. s : Scissors\n"
                      "2. r : Rock\n"
                      "3. p : Paper\n")

    # Randomly select the computer's choice from 'r', 'p', 's'
    computer_turn = random.choice(['r', 'p', 's'])
    print("Computer's Choice: ", computer_turn)  # Display the computer's choice

    # Check for a tie
    if user_turn == computer_turn:
        return "It's a TIE"

    # Check if the user won
    if is_win(user_turn, computer_turn):
        return "YOU WON!!!"

    # If it's not a tie and the user didn't win, the user lost
    return "YOU LOST!!!"

def is_win(player, opponent):
    """
    Function to determine if the player has won.
    Args:
    player (str): The player's move.
    opponent (str): The opponent's (computer's) move.

    Returns:
    bool: True if the player wins, False otherwise.
    """
    # Define the winning conditions: rock beats scissors, scissors beat paper, paper beats rock
    if (player == 'r' and opponent == 's') or \
       (player == 's' and opponent == 'p') or \
       (player == 'p' and opponent == 'r'):
        return True
    return False  # If none of the winning conditions are met, return False

def main():
    """
    Main function to run the Rock, Paper, Scissors game in a loop.
    """
    while True:  # Loop to allow multiple rounds of the game
        result = play()  # Play one round and get the result
        print(result)  # Print the result of the round
        # Ask the user if they want to play again
        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != 'y':  # If the user does not enter 'y', break the loop
            break

# Entry point of the script
if __name__ == "__main__":
    main()  # Call the main function to start the game
