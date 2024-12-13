# Reads the entire contents of a file
def read_from_file(name):
   with open(name) as file:
      content = file.read()
   return content

# reads the entire file and splits lines into an array
file_content = read_from_file('pets.txt')
file_lines = file_content.splitlines()

total_words = 0

# print each line and count the words
for line in file_lines:
    print(line)
    words_in_line = line.split() 
    total_words += len(words_in_line) 

print('Total number of words:', total_words)
