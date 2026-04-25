from utils import books, Book

def show_books():
    if not books:
        print("\nNo books available in the library.\n")
        return
        
    print("\n====== BOOKS AVAILABLE IN THE LIBRARY ======\n")
    print("| TITLE | AUTHOR | COUNT | ")
    l=[]
    for i in books.values():
        if i.status == "available":
            if (i.name,i.author) not in l:
                print(f"| {i.name} | {i.author} | {i.count_book()} |")
                l.append((i.name,i.author))
    print("\n============================================\n")