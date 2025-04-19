def num_in_stock(fruit):
    """
    Returns the number of the given fruit in stock.
    """
    inventory = {
        "apple": 50,
        "banana": 100,
        "pear": 1000,
        "orange": 200,
        "grape": 300
    }
    return inventory.get(fruit, 0)  # Return the count if the fruit exists, otherwise 0

def main():
    # Prompt the user to enter a fruit
    fruit = input("Enter a fruit: ").lower()  # Convert input to lowercase for consistency
    
    # Call num_in_stock to get the number of that fruit in stock
    stock = num_in_stock(fruit)
    
    # Check if the fruit is in stock
    if stock > 0:
        print("This fruit is in stock! Here is how many:")
        print(stock)
    else:
        print("This fruit is not in stock.")

if __name__ == '__main__':
    main()
    