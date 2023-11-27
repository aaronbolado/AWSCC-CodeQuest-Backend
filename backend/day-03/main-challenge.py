

print("\nWelcome, little red riding hood! What should we call you?")
username = input("\nEnter your username: ")

print(f"\nGreat! Now, {username}, do you want to continue to the dangerous forest?")
answer = input("\nYES or NO: ")

if answer == "YES":
    print("\nBIG BAD WOLF APPEARED! Do you choose to run?")
    answer = input("\nYES or NO: ")
    if answer == "YES":
        print("\nBIG BAD WOLF CAUGHT UP TO YOU! GAME OVER!\n")
    else:
        print("\nYou stood your ground and summoned... Tiamat O_O a bit overkill... BUT YOU WIN!!\n")
else:
    print("\nThere seems to be an old lady in need of help. Do you go to her?")
    answer = input("\nYES or NO: ")
    if answer == "YES":
        print("\nIT'S THE BIG BAD WOLF IN DISGUISE! GAME OVER!\n")
    else: 
        print("\nYou got home safely! YOU WIN!!\n")