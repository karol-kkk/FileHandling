###
# Reads from file, line by line
#
with open('countries.txt', 'r') as file:
    for idx, line in enumerate(file, start=1):
        print(f"{idx}. {line.strip()}")
