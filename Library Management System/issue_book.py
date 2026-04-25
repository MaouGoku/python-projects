from utils import books, Book
import datetime as dt

def issue_book():
    book_name = input("Enter the name of the book you want to issue: ").strip().upper()
    author_name = input("Enter the name of the author: ").strip().upper()
    student_name = input("Enter your name: ").strip().upper()
    roll_number = input("Enter your roll number: ").strip().upper()
    issue_date =  dt.datetime.now().date()
    
    # Checks if the student has already issued the same book
    Verify_issued = [i for i in books.values() if i.name == book_name and i.author == author_name and i.status == "issued" and i.issued_roll == roll_number and i.issued_by == student_name]
    if Verify_issued:
        print(f"{student_name} has already issued '{book_name}' by {author_name} (ID: {Verify_issued[0].id}) on {Verify_issued[0].issue_date.strftime('%d-%m-%Y')}. Due date: {Verify_issued[0].return_date.strftime('%d-%m-%Y')}.")
        return    

    # Checks if the book is available and prints all the available books with the same name and author
    match = [i for i in books.values() if i.name == book_name and i.author == author_name and i.status == "available"]
    
    #Displays all the available books with the same name and author
    for i in match:
        print(i)
    #Issues the book to the student if available
    if match:
        match[0].status = "issued"
        match[0].issued_by = student_name
        match[0].issued_roll = roll_number
        match[0].issue_date = issue_date
        match[0].return_date = issue_date + dt.timedelta(days=7)
        print(f"{student_name} have issued '{match[0].name}' by {match[0].author} (ID: {match[0].id}) on {match[0].issue_date.strftime("%d-%m-%Y")}. Due date: {match[0].return_date.strftime("%d-%m-%Y")}.")
        print("""
Fine Policy:
A late return will incur a progressive fine calculated as follows:

Week 1: ₹10 per day per book
Week 2: ₹10*2 per day per book
Week 3: ₹10*2*3 per day per book
Subsequent weeks: The daily fine increases multiplicatively (₹10 × 1 × 2 × 3 × … per week).
The total fine is computed cumulatively based on the number of overdue days.
""")
        return
    print(f"Sorry, '{book_name}' by {author_name} is not available.")