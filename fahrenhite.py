def main():
    print("Temperature in fahrenhiet! ")
    fahrenheit = float(input("Enter the temeprature in fahrenheit: "))
    celsius = (fahrenheit - 32) * 5.0 / 9,0
    print(f"Temperature: {fahrenheit}F = {celsius}C")
    
    #This provided line is required at theend of
    #python file to call the main() function.
if __name__ == '__main__':
    main()   