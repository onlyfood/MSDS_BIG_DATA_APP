import requests
from .models import Book

def fetch_data_and_store_in_db():
    # Make a request to the API
    response = requests.get('https://api.example.com/books')

    # Process the API response and extract the data
    data = response.json()

    # Iterate over the data and create Book objects
    for book_data in data:
        book = Book(
            title=book_data['title'],
            author=book_data['author'],
            publication_date=book_data['publication_date'],
            # Set other fields accordingly
        )
        book.save()
