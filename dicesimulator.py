import random

def roll_dice():
    # Local variables for dice rolls
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1, die2

# Simulate rolling dice three times
for i in range(1, 4):
    die1, die2 = roll_dice()  # Call the function to roll dice
    print(f"Roll {i}: Die 1 = {die1}, Die 2 = {die2}")

# Note: 'die1' and 'die2' inside the function are local to it,
# while the ones in the loop are in the global scope.