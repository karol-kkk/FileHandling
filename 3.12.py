import csv

# Function to read books from the CSV file
def read_books_from_csv(file_name):
    with open(file_name, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)

# Function to filter books by genre
def filter_books_by_genre(books, genre):
    return [book for book in books if book['Genre'].lower() == genre.lower()]

# Function to save books to a text file
def save_books_to_file(books, genre):
    filename_map = {
        'Fantasy': 'books_fantasy.txt',
        'Historical': 'books_historical.txt',
        'Romance': 'books_romance.txt',
        'Classic': 'books_classic.txt'
    }

    filename = filename_map.get(genre)
    if filename:
        with open(filename, 'w', encoding='utf-8') as file:
            for book in books:
                file.write(f"{book['Title']},{book['Author']},{book['Genre']},{book['Year']}\n")
        print(f"Books in the genre '{genre}' have been saved to {filename}")
    else:
        print(f"Genre '{genre}' is not supported.")

# Taking user input and processing
csv_filename = 'books.csv'  # The input CSV file containing book data
genre = input("Enter the genre (Fantasy, Historical, Romance, Classic): ").strip()

books = read_books_from_csv(csv_filename)
filtered_books = filter_books_by_genre(books, genre)

if filtered_books:
    save_books_to_file(filtered_books, genre)
else:
    print(f"No books found for genre '{genre}'")
