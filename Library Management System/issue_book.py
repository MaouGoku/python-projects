from utils import books, issued_books

def issue_book():
    book_name = input("Enter the name of the book you want to issue: ").strip().upper()
    # for book in books:
    # if book['name'] == book_name:
    if book_name in books:
        issued_books.append(book_name)
        books.remove(book_name)
        print(f"You have issued '{book_name}'.")
        return
    print(f"Sorry, '{book_name}' is not available.")