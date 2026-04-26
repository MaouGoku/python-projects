from utils import books

def show_books():
    # Checks if books are added or not 
    if not books:
        print("\nNo books added in the library.\n")
        return

    # Fetches available books in library 
    available = [b for b in books.values() if b.status == "available"]
    
    # if all books are issued 
    if not available:
        print("\nAll books are issued.\n")
        return
    
    # Makes unique books
    unique = {(b.name, b.author): b for b in available}
    
    # Variables for Menu Design  
    padding = 4
    title_width = max(len(b.name) for b in unique.values()) + padding
    author_width = max(len(b.author) for b in unique.values()) + padding
    count_width = max(len(str(b.count_book())) for b in unique.values()) + padding

    header = f"║ {'TITLE':^{title_width}} ║ {'AUTHOR':^{author_width}} ║ {'COUNT':^{count_width}} ║"
    top = "╔"+"═"*(title_width+2)+"╦"+"═"*(author_width+2)+"╦"+"═"*(count_width+2)+"╗"
    middle = "╠"+"═"*(title_width+2)+"╬"+"═"*(author_width+2)+"╬"+"═"*(count_width+2)+"╣"
    bottom = "╚"+"═"*(title_width+2)+"╩"+"═"*(author_width+2)+"╩"+"═"*(count_width+2)+"╝"
    decorator = f"<<{' LIBRARY ':-^{len(top)-4}}>>"

    # Menu Display Sequence
    print("\nThe available books are listed below:\n")
    print(decorator)
    print(top)
    print(header)
    print(middle)

    for i in unique.values():
        print(f"║ {i.name : ^{title_width}} ║ {i.author : ^{author_width}} ║ {i.count_book() : ^{count_width}} ║")
    print(bottom)
