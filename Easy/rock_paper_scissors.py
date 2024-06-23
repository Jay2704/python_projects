import random

def play():
    user_turn = input("Enter\n"
                       "1. s : Scissors\n"
                       "2. r : Rock\n"
                       "3. p : Paper\n")

    computer_turn = random.choice(['r', 'p', 's'])
    print("Computer's Choice: ", computer_turn)
    if user_turn == computer_turn:
        return "It's a TIE"

    if is_win(user_turn, computer_turn):
        return "YOU WON!!!"

    return "YOU LOST!!!"

def is_win(player, opponent):
    # rock beats scissors, scissor beats paper, paper beats rock

    if (player == 'r' and opponent == 's') or \
            (player == 's' and opponent == 'p') or \
            (player == 'p' and opponent == 'r'):
        return True


    else:
        return False



def main():
    while True:
        result = play()
        print(result)
        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != 'y':
            break

if __name__ == "__main__":
    main()



