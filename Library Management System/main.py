from add_book import add_book
from show_books import show_books
from issue_book import issue_book
from return_book import return_book
from book_status import book_status

   
   
def library():
    while True:
        print('''
====== LIBRARY MENU ======
1. Add Book
2. Show Books
3. Issue Book
4. Return Book
5. Check Book Status
6. Exit
              ''')
        menu = {
            1: add_book,
            2: show_books,
            3: issue_book,
            4: return_book,
            5: book_status
        }

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 6:
            print("Thank you for using the library management system.")
            break

        action = menu.get(choice)

        if action:
            action()
    else:
        print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    #Function Call
    library()


