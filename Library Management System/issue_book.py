from utils import books, Book
import datetime as dt

def issue_book():
    book_name = input("Enter the name of the book you want to issue: ").strip().upper()
    author_name = input("Enter the name of the author: ").strip().upper()
    student_name = input("Enter your name: ").strip().upper()
    roll_number = input("Enter your roll number: ").strip().upper()
    issue_date =  dt.datetime.now().date()
    
    match = [i for i in books.values() if i.name == book_name and i.author == author_name and i.status == "available"]
    
    for i in match:
        print(i)

    if match:
        match[0].status = "issued"
        match[0].issued_by = student_name
        match[0].issued_roll = roll_number
        match[0].issue_date = issue_date
        match[0].return_date = issue_date + dt.timedelta(days=7)
        print(f"{student_name} have issued '{match[0].name}' (ID: {match[0].id}) on {match[0].issue_date.strftime("%d-%m-%Y")}. Due date: {match[0].return_date.strftime("%d-%m-%Y")}.")
        return
    print(f"Sorry, '{book_name}' is not available.")