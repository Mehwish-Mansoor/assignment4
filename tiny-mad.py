def main():
    # Constants
    SENTENCE_START = "Code in Place is fun. I learned to program and used Python to make my"

    # Prompt the user for an adjective, noun, and verb
    adjective = input("Please type an adjective and press enter: ")
    noun = input("Please type a noun and press enter: ")
    verb = input("Please type a verb and press enter: ")

    # Construct and print the final sentence
    print(f"{SENTENCE_START} {adjective} {noun} {verb}.")

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()