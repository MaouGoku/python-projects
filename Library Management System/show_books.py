from utils import books, book_inventory

def show_book():
    if not book_inventory:
        print("\nNo books available in the library.\n")
        return
    print("\n====== Books available in the library ======\n")

    for (name, author), count in book_inventory.items():
        print(f"- {name} by {author} | Available: {count}")