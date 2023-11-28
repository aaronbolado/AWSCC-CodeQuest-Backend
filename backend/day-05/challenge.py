import random

print("\nROCK PAPER SCISSORS GAME")

options_list = ["rock", "paper", "scissor"]

player1 = random.choice(options_list)


player2 = input("\nPlayer2: ").lower()
print(f"Player1: {player1}")

if player2 == player1:
    print("\nDraw!")
elif (player2 == "rock" and player1 == "scissor") or (player2 == "paper" and player1 == "rock") or (player2 == "scissor" and player1 == "paper") :
    print("\nPlayer2 Wins!")
else:
    print("\nPlayer1 Wins!")

