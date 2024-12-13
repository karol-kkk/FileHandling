def count_file_contents(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()  # Read all lines from the file
            num_lines = len(lines)
            num_characters = sum(len(line) for line in lines)  # Sum up the length of each line
            num_words = sum(len(line.split()) for line in lines)  # Split each line into words and count them

        return num_lines, num_characters, num_words

    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
        return None, None, None

# Main program
file_name = input("Enter the file name: ")

num_lines, num_characters, num_words = count_file_contents(file_name)

if num_lines is not None:
    print(f"File name: {file_name}")
    print(f"Number of lines: {num_lines}")
    print(f"Number of characters: {num_characters}")
    print(f"Number of words: {num_words}")
