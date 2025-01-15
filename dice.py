import random
# Function to simulate rolling the dice
def roll_dice():
    return random.randint(1, 6)
# Main program loop
while True:
    # Ask the user if they want to roll the dice
    user_input = input("Do you want to roll the dice? (yes/no): ").lower()
    
    # Check if the user wants to roll the dice
    if user_input == 'yes':
        print(f"🎲 You rolled a {roll_dice()}! 🎲")
    elif user_input == 'no':
        print("Thanks for playing! Goodbye.")
        break
    else:
        print("Invalid input. Please type 'yes' or 'no'.")