from utils import books, book_inventory

def show_book():
    if len(books) == 0:
        print("No books available in the library.")
    else:
        print("Books available in the library:")
        for book in books.values():
            print(f"- {book['name']} by {book['author']} | Stock: {book_inventory[book['name']]} | Issued: {'Yes' if book['issued'] else 'No'}")
            
        # for index, book in enumerate(books, start=1):
        #     print(f"{index}. {book}")
    