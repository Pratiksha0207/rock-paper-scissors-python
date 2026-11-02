import random

print("Rock, Paper, Scissor Game Started!")

# List of game images/emojis

game_images = ["Rock 🪨", "Paper 📄", "Scissors ✂"]

# The try block checks the code inside it for any input errors

try:
    User_Choice = int(input("Enter your Choice: Type 0 for Rock, 1 for Paper, 2 for Scissors: "))

    # First we validate the user input to prevent index crash errors

    if User_Choice >= 3 or User_Choice < 0:
        print("YOU ENTERED INVALID NUMBER, YOU LOSE!")
    else:
        # Print the choices and execute computer's turn only if input is valid
        print(f"You chose: {game_images[User_Choice]}")
        
        Computer_Choice = random.randint(0, 2)
        print(f"Computer chose: {game_images[Computer_Choice]}")

        # Win/Lose/Draw comparison logic nested inside the else block
        
        if Computer_Choice == User_Choice:
            print("IT'S A DRAW 🤝")
        elif Computer_Choice == 0 and User_Choice == 2:
            print("YOU LOSE 😢")
        elif User_Choice == 0 and Computer_Choice == 2:
            print("YOU WIN 🎉")    
        elif Computer_Choice > User_Choice:
            print("YOU LOSE 😢")
        elif User_Choice > Computer_Choice:
            print("YOU WIN 🎉")

# If the user types text/alphabets, this block catches the ValueError and prevents a crash

except ValueError:
    print("❌ ERROR: Please enter a valid number (0, 1, or 2) only! Alphabets or symbols are not allowed.")
