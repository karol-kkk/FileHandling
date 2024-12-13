# Prints employees employed in a specified position.
#
# Employee List
file_name = 'it_company.csv'

# Position
job_title = 'Software Engineer'

with open(file_name, 'r') as file:
    # Initialize a counter to number the employees
    count = 1
    
    for line in file:
        # Split the line into parts
        parts = line.strip().split(',')
        
        # Check if the job title is "Software Engineer"
        if job_title in parts[2]:
            print(f"{count}. {line.strip()}")
            count += 1