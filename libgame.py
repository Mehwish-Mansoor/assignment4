# Mad Libs Project

# Get user inputs
name = input("Enter a name: ")
place = input("Enter a place: ")
adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")

# Create the Mad Libs story using f-strings
mad_lib = f"One day, {name} went to {place}. It was a very {adjective} day. \
While there, {name} found a {noun} and decided to {verb} it. What an adventure!"

# Print the story
print("\nHere is your Mad Libs story:")
print(mad_lib)