import csv

def filter_clothing(csv_filename):
    # Open the CSV file
    with open(csv_filename, mode='r') as file:
        reader = csv.DictReader(file)
        
        print("Products with Price < 60 and Stock Quantity < 40:")
        print("===================================================")
        
        # Iterate over each row in the CSV file
        for row in reader:
            # Convert price and stock quantity to float and int for comparison
            price = float(row['Price'])
            stock_quantity = int(row['Stock_Quantity'])
            
            # Check if the product's price is less than 60 and stock is less than 40
            if price < 60 and stock_quantity < 40:
                # Print the product details (Product_Name, Price, Stock_Quantity)
                print(f"{row['Product_Name']} - ${price} - Stock: {stock_quantity}")

# Call the function and pass the file name
filter_clothing('clothing.csv')
