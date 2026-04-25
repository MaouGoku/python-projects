from utils import books, Book
import datetime as dt

def return_book():
    book_name = input("Enter the name of the book you want to return: ").strip().upper()
    author_name = input("Enter the name of the author: ").strip().upper()
    student_name = input("Enter your name: ").strip().upper()
    roll_number = input("Enter your roll number: ").strip().upper()

    # Check if the student has issued the book
    match = [i for i in books.values() if i.name == book_name and i.author == author_name and i.status == "issued" and i.issued_roll == roll_number and i.issued_by == student_name]
    
    if match:
        return_date_now = dt.datetime.now().date()
        match[0].finecalc()
        fine_amount = match[0].fine
        
        match[0].status = "available"
        match[0].issued_by = None
        match[0].issued_roll = None
        match[0].issue_date = None
        match[0].return_date = None
        match[0].fine = 0
        
        print(f"{student_name} have returned '{match[0].name}' by {match[0].author} (ID: {match[0].id}) on {return_date_now.strftime('%d-%m-%Y')}.")
        if fine_amount != 0:
            print(f"Fine: Rs. {fine_amount}")
        return

    print(f"Sorry, '{book_name}' by {author_name} is not issued to you.")
    
    