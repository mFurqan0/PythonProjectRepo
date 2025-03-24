import random 

dice_messages = {
    1: "SAD!",
    2: "Not bad! Keep going!",
    3: "You are doing great!",
    4: "Damn! You are on fire!",
    5: "You are a pro!",
    6: "Perfect Six!"
}


def dice_simulator():
    

    for i in range(1, 11):
        roll_dice = random.randint(1, 6)
        print(f"Roll {i}: You rolled a {roll_dice} - {dice_messages[roll_dice]}")
        
dice_simulator()