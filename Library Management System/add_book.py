from utils import books, book_inventory
import random

def add_book():
    book_name = input("Enter the name of the book: ").strip().upper()
    author_name = input("Enter the name of the author: ").strip().upper()
    book_id = random.randint(1000, 9999)
    books[book_id] = {
        "name": book_name,
        "author": author_name,
        "issued": False
    }
    for book in books.values():
        if book["name"] not in book_inventory:
            book_inventory[book["name"]] = 1
    else:
        book_inventory[book["name"]] += 1 
    print(f"Book '{book_name}' by {author_name} added successfully with ID {book_id}.")
    
    # author_name = input("Enter the name of the author: ")
    # book_id = len(books) + 1
    # book_details = {
    #     "id": book_id,
    #     "name": book_name,
    #     "author": author_name,
    #     "issued": False
    # }
    # books.append(book_details)
    # print(f"Book '{book_name}' by {author_name} added successfully with ID {book_id}.")