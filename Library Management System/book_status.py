from utils import books

def book_status():
    # show list that which by which author got issued to whom and when
    print("""\n====== BOOK STATUS ======\n""")
    for i in books.values():
        if i.status == "issued":
            print(f"ID: {i.id} | Title: {i.name} | Author: {i.author} | Issued To: {i.issued_by} | Roll No: {i.issued_roll} | Issue Date: {i.issue_date} | Return Date: {i.return_date}")
    print("""\n========================\n""")
    return