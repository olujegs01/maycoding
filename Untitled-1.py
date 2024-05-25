def main():
    while True:
        print("Choose an option:")
        print("1. Calculate the square footage of a house")
        print("2. Calculate the circumference of a circle")
        print("3. Quit")
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            try:
                length = float(input("Enter the length of the house: "))
                width = float(input("Enter the width of the house: "))
                area = geometry.square_footage(length, width)
                print(f"The square footage of the house is {area:.2f} square units.")
            except ValueError:
                print("Invalid input. Please enter numerical values for length and width.")
                
        elif choice == '2':
            try:
                radius = float(input("Enter the radius of the circle: "))
                circ = geometry.circumference(radius)
                print(f"The circumference of the circle is {circ:.2f} units.")
            except ValueError:
                print("Invalid input. Please enter a numerical value for radius.")
                
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

# Run the main program
main()
