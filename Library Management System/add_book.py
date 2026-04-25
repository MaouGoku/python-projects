from utils import books, Book
import random

def add_book():
    book_name = input("Enter the name of the book: ").strip().upper()
    author_name = input("Enter the name of the author: ").strip().upper()
    book_id = random.randint(1000, 9999)
    while book_id in books:
        book_id = random.randint(1000, 9999)
        
    books[book_id] = Book(book_id, book_name, author_name)
    
    print(f"Book '{book_name}' by {author_name} added successfully with ID {book_id}.")
    
