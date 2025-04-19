def even_or_odd(start, end):
    """
    Prints whether each number in the range [start, end] is even or odd.
    """
    for num in range(start, end + 1):
        if num % 2 == 0:
            print(f"{num} even", end=" ")
        else:
            print(f"{num} odd", end=" ")

# Example usage
if __name__ == "__main__":
    even_or_odd(10, 49)