import random

n = 'Not Again!'

while True:
    user = input("Enter a choice (rock, paper, scissors, lizard, spoke):\n>>> ")
    possible_actions = ["rock", "paper", "scissors" , "lizard" , "spoke"]
    results = [[0, -1, 1, -1, 1],  # rock
               [1, 0, -1, 1, -1],  # paper
               [-1, 1, 0, -1, -1],  # scissors
               [1, -1, 1, 0, 1],  # lizard
               [-1, 1, 1, -1, 0]]
    answers = ["y" , "n"]
    computer = random.choice(possible_actions)
    if user not in possible_actions:
        print(f'Invalid input "{user}"')
        continue
    print(f"\nYou chose: {user}\nComputer chose: {computer}\n")
    index_user = possible_actions.index(user)
    index_computer = possible_actions.index(computer)

    result = results[index_user][index_computer]
    if (result < 0):
        print('You lose')
    elif (result > 0):
        print('You win!')
    else:
        print('Draw')

    while True:
        play_again = input("Play again? (y/n):\n>>>")
        if play_again == "y":
            break
        if play_again not in answers:
            print(f'Invalid input "{play_again}"')
            continue
        if play_again == "n":
            print(f'Invalid input "{n}"')