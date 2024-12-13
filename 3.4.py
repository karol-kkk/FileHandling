def display_lines(filename="it_company.csv"):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            
            # Set the starting index for the first 5 lines
            start_index = 0
            while start_index < len(lines):
                # Get the next 5 lines
                end_index = min(start_index + 5, len(lines))
                for line in lines[start_index:end_index]:
                    print(line, end="")  # Print the line without adding an extra newline
                print("\nPress Enter key...")  # Prompt for the next batch of lines
                input()  # Wait for the Enter key to be pressed
                start_index = end_index  # Update the starting index for the next 5 lines
                
    except FileNotFoundError:
        print("The file does not exist. Please check the file path and name.")

# Call the function to display the lines from 'it_company.csv'
display_lines()