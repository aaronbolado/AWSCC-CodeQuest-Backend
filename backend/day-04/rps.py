print("SIMPLE ROCK PAPER SCISSORS GAME")
player1 = "rock"
print(f"\nPlayer1: {player1}")
player2 = input("Player2: ")


if player2 == player1:
    print("\nDraw!")
elif player2 == "scissors":
    print("\nPlayer1 Wins!")
else:
    print("\nPlayer2 Wins!")

