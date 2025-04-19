def main():
    # Dictionary of fruits and their prices
    fruit_prices = {
        "apple": 100.00,
        "banana": 150.00,
        "strawberries": 200.00,
        "kiwi": 300.0,
        "pear": 150.00,
        "mango": 200.00
    }

    total_cost = 0  # Initialize total cost

    # Loop through the dictionary to ask the user how many of each fruit they want
    for fruit, price in fruit_prices.items():
        quantity = int(input(f"How many ({fruit}) do you want?: "))
        total_cost += quantity * price  # Add the cost of the current fruit to the total

    # Print the total cost
    print(f"\nYour total is {total_cost:.2f}")

if __name__ == '__main__':
    main()