from utils import books

# show list that which by which author got issued to whom and when
def book_status():
    # Fetches list of issued books
    issued = [b for b in books.values() if b.status == "issued"]
    
    # if no books are issued
    if not issued:
        print("\nNo books are issued.\n")
        return

    # Calculates fine for each issued book
    for i in issued:
        i.finecalc()

    # Variables for Menu Design  
    padding = 4
    title_width = max(len(b.name) for b in issued) + padding
    author_width = max(len(b.author) for b in issued) + padding
    id_width = max(len(str(b.id)) for b in issued) + padding
    issue_width = max(len(str(b.issued_by)) for b in issued) + padding
    roll_width = max(len(str(b.issued_roll)) for b in issued) + padding
    issue_date_width = max(len(i.strftime('%d-%m-%Y')) for i in [b.issue_date for b in issued]) + padding
    return_date_width = max(len(i.strftime('%d-%m-%Y')) for i in [b.return_date for b in issued]) + padding
    fine_width = max(len(str(b.fine)) for b in issued) + padding
    fine_width = max(fine_width, len("FINE") + padding)

    header = f"║ {'TITLE':^{title_width}} ║ {'AUTHOR':^{author_width}} ║ {'ID':^{id_width}} ║ {'ISSUED TO':^{issue_width}} ║ {'ROLL NO':^{roll_width}} ║ {'ISSUE DATE':^{issue_date_width}} ║ {'RETURN DATE':^{return_date_width}} ║ {'FINE':^{fine_width}} ║"
    top = "╔"+"═"*(title_width+2)+"╦"+"═"*(author_width+2)+"╦"+"═"*(id_width+2)+"╦"+"═"*(issue_width+2)+"╦"+"═"*(roll_width+2)+"╦"+"═"*(issue_date_width+2)+"╦"+"═"*(return_date_width+2)+"╦"+"═"*(fine_width+2)+"╗"
    middle = "╠"+"═"*(title_width+2)+"╬"+"═"*(author_width+2)+"╬"+"═"*(id_width+2)+"╬"+"═"*(issue_width+2)+"╬"+"═"*(roll_width+2)+"╬"+"═"*(issue_date_width+2)+"╬"+"═"*(return_date_width+2)+"╬"+"═"*(fine_width+2)+"╣"
    bottom = "╚"+"═"*(title_width+2)+"╩"+"═"*(author_width+2)+"╩"+"═"*(id_width+2)+"╩"+"═"*(issue_width+2)+"╩"+"═"*(roll_width+2)+"╩"+"═"*(issue_date_width+2)+"╩"+"═"*(return_date_width+2)+"╩"+"═"*(fine_width+2)+"╝"
    decorator = f"<<{' BOOK STATUS ':-^{len(top)-4}}>>"

    # Menu Display Sequence
    print("\nThe issued books are listed below:\n")
    print(decorator)
    print(top)
    print(header)
    print(middle)

    for i in issued:
        print(f"║ {i.name : ^{title_width}} ║ {i.author : ^{author_width}} ║ {i.id : ^{id_width}} ║ {i.issued_by : ^{issue_width}} ║ {i.issued_roll : ^{roll_width}} ║ {i.issue_date.strftime('%d-%m-%Y') : ^{issue_date_width}} ║ {i.return_date.strftime('%d-%m-%Y') : ^{return_date_width}} ║ {i.fine : ^{fine_width}} ║")
    print(bottom)