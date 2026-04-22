from add_book import add_book
from show_book import show_book
from issue_book import issue_book
from return_book import return_book
# from book_status import book_status

   
   
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
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_book()
        elif choice == 2:
            show_book()
        elif choice == 3:
            issue_book()
        elif choice == 4:
            return_book()
        elif choice == 5:
            book_status()
        elif choice == 6:
            print("Thank you for using the library management system.")
            break
        else:
            print("Invalid choice. Please try again.")
            
#Function Call
library()


