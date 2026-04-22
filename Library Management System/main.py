from add_book import add_book
from show_book import show_book
from issue_book import issue_book
from return_book import return_book
from utils import books
   

def library():
    while True:
        print("\n1. Add Book")
        print("\n2. Show Books")
        print("\n3. Issue Book")
        print("\n4. Return Book")
        print("\n5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_book()
        elif choice == 2:
            show_book()
        elif choice == 3:
            issue_book()
        elif choice == 4:
            return_book()
            # print(books.items())
        elif choice == 5:
            print("Thank you for using the library management system.")
            break
        else:
            print("Invalid choice. Please try again.")
            
#Function Call
library()


