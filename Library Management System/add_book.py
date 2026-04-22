from utils import books, book_inventory
import random

def add_book():
    book_name = input("Enter the name of the book: ").strip().upper()
    author_name = input("Enter the name of the author: ").strip().upper()
    book_id = random.randint(1000, 9999)
    while book_id in books:
        book_id = random.randint(1000, 9999)
        
    books[book_id] = {
        "name": book_name,
        "author": author_name,
        "available": True,
        "issue": None      
    }
    
    key = (book_name, author_name)
    if key not in book_inventory:
        book_inventory[key] = 1
    else:
        book_inventory[key] += 1
        
    print(f"Book '{book_name}' by {author_name} added successfully with ID {book_id}.")
    
