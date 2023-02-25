import random

n = 'Not Again!'

while True:
    user = input("Enter a choice (rock, paper, scissors, lizard, spoke):\n>>> ")
    possible_actions = ["rock", "paper", "scissors" , "lizard" , "spoke"]
    answers = ["y" , "n"]
    computer = random.choice(possible_actions)
    if user not in possible_actions:
        print(f'Invalid input "{user}"')
        continue
    print(f"\nYou chose: {user}\nComputer chose: {computer}\n")
    if user == computer:
        print(f"Both players selected {user} . Draw!")
    elif user == "rock":
        if computer == "scissors":
            print("You win!")
        else:
            print("You lose.")
    elif user == "paper":
        if computer == "rock":
            print("You win!")
        else:
            print("You lose.")
    elif user == "scissors":
        if computer == "paper":
            print("You win!")
        else:
            print("You lose.")
    elif user == "lizard":
        if computer == "scissors":
            print("You lose.")
        else:
            print("You win!")
    elif user == "spoke":
        if computer == "stone":
            print("You win!")
        else:
            print("You lose")

    while True:
        play_again = input("Play again? (y/n):\n>>>")
        if play_again == "y":
            break
        if play_again not in answers:
            print(f'Invalid input "{play_again}"')
            continue
        if play_again == "n":
            print(f'Invalid input "{n}"')



