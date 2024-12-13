def calculate_powers():
    # Open a text file in write mode
    with open('powers.txt', 'w') as file:
        # Iterate through numbers 1 to 100
        for i in range(1, 101):
            second_power = i ** 2  # Calculate the second power
            third_power = i ** 3   # Calculate the third power
            
            # Print the result
            print(f"{i},{second_power},{third_power}")
            
            # Write the result to the file
            file.write(f"{i},{second_power},{third_power}\n")

# Call the function
calculate_powers()
