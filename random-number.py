import random  # Import the random module to generate random numbers

def main():
    # Print 10 random numbers in the range 1 to 100
    for _ in range(10):  # Loop 10 times
        print(random.randint(1, 100), end=" ")  # Generate and print a random number

if __name__ == '__main__':
    main()