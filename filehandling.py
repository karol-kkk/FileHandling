# 1.6
# Reads the entire contents of a file
#
def read_from_file(name):
   with open(name, 'r') as file:
      content = file.read()
   return content

# reads the entire file
file_content = read_from_file('countries.txt')

# splits the entire file contents into lines
# and stores them in an array
file_lines = file_content.splitlines()

# sort the list alphabetically
file_lines_sorted = sorted(file_lines)

# prints the sorted array
for line in file_lines_sorted:
   print(line)


