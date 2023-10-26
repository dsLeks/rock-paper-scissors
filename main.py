import random

valid_moves = ['rock', 'paper', 'scissors']

user_move = input("Enter your move (rock, paper, scissors): ")
while user_move not in valid_moves:
    user_move = input("Invalid move. Enter your move (rock, paper, scissors): ")

computer_move = random.choice(valid_moves)

print(f"You played {user_move}. The computer played {computer_move}.")

if user_move == computer_move:
    print("It's a tie!")
elif (user_move == 'rock' and computer_move == 'scissors') or \
     (user_move == 'paper' and computer_move == 'rock') or \
     (user_move == 'scissors' and computer_move == 'paper'):
    print("You win!")
else:
    print("The computer wins!")
