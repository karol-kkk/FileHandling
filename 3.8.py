import re

def filter_files_by_extension(file_name):
    # Regular expression to match file extensions with exactly 4 characters (e.g. .html)
    return bool(re.search(r'\.[a-zA-Z]{4}$', file_name))

# Read the file names from 'files.txt' and filter based on the extension length
try:
    with open('files.txt', 'r') as file:
        file_names = file.readlines()
        
    # Strip any extra whitespace/newlines and filter filenames based on extension length
    for file_name in file_names:
        file_name = file_name.strip()  # Remove leading/trailing spaces or newlines
        if filter_files_by_extension(file_name):
            print(file_name)
except FileNotFoundError:
    print("Error: 'files.txt' not found.")
