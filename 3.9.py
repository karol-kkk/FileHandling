import csv

def find_graphic_designers(csv_filename):
    graphic_designers = []

    try:
        with open(csv_filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            # Iterate through each row and check the job title
            for row in reader:
                if row['Job Title'] == 'Graphic Designer':
                    first_name = row['First Name']
                    last_name = row['Last Name']
                    email = row['Email']
                    graphic_designers.append(f"{first_name} {last_name},{email}")

        # Print the results
        print("GRAPHIC DESIGNERS")
        print("=================")
        for designer in graphic_designers:
            print(designer)

    except FileNotFoundError:
        print(f"Error: {csv_filename} not found.")

# Specify the CSV file name
csv_filename = 'it_company.csv'
find_graphic_designers(csv_filename)
