from utils import books, issued_books

def return_book():
    book_name = input("Enter the name of the book you want to return: ").strip().upper()
    if book_name in issued_books:
        issued_books.remove(book_name)
        books.append(book_name)
        print(f"You have returned '{book_name}'.")
        return
    print(f"Sorry, '{book_name}' is not available.")