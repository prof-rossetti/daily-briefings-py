





def approach_1(user_choice, computer_choice):
    if user_choice == "rock":
        if computer_choice == "rock":
            winning_choice = None
        elif computer_choice == "paper":
            winning_choice = "paper"
        elif computer_choice == "scissors":
            winning_choice = "rock"
    elif user_choice == "paper":
        if computer_choice == "rock":
            winning_choice = "paper"
        elif computer_choice == "paper":
            winning_choice = None
        elif computer_choice == "scissors":
            winning_choice = "rock"
    elif user_choice == "scissors":
        if computer_choice == "rock":
            winning_choice = "rock"
        elif computer_choice == "paper":
            winning_choice = "scissors"
        elif computer_choice == "scissors":
            winning_choice = None
    return winning_choice


def approach_2(user_choice, computer_choice):
    if user_choice == computer_choice:
        winning_choice = None # represents a tie
    elif computer_choice == "rock" and user_choice == "scissors":
        winning_choice = computer_choice
    elif computer_choice == "scissors" and user_choice == "rock":
        winning_choice = user_choice
    elif computer_choice == "paper" and user_choice == "rock":
        winning_choice = computer_choice
    elif computer_choice == "rock" and user_choice == "paper":
        winning_choice = user_choice
    elif computer_choice == "scissors" and user_choice == "paper":
        winning_choice = computer_choice
    elif computer_choice == "paper" and user_choice == "scissors":
        winning_choice = user_choice
    return winning_choice


def approach_3(user_choice, computer_choice):
    winners = {
        "rock": {
            "rock": None,
            "paper": "paper",
            "scissors": "rock",
        },
        "paper": {
            "rock": "paper",
            "paper": None,
            "scissors": "scissors",
        },
        "scissors": {
            "rock": "rock",
            "paper": "scissors",
            "scissors": None,
        }
    }
    winning_choice = winners[user_choice][computer_choice]
    return winning_choice





if __name__ == "__main__":
    u = "rock"
    c = "paper"

    print("------------------")
    print("USER CHOICE:", u)
    print("COMPUTER CHOICE", c)
    print("------------------")
    print("WINNER: (APPROACH 1)", approach_1(u, c))
    print("WINNER: (APPROACH 2)", approach_2(u, c))
    print("WINNER: (APPROACH 3)", approach_3(u, c))
