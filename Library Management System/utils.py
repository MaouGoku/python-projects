# Main Data Storage
import datetime as dt
import math

class Book:
    def __init__(self, id, name, author):
        self.id = id
        self.name = name
        self.author = author
        self.status = "available"
        self.issue_date = None
        self.return_date = None
        self.issued_by = None
        self.issued_roll = None
        self.fine = 0
    def __str__(self):
        return f"ID: {self.id} | Title: {self.name} | Author: {self.author} | Status: {self.status}"

    def finecalc(self):
        if self.status == "issued":
            if dt.datetime.now().date() > self.return_date:
                late_days = (dt.datetime.now().date() - self.return_date).days
                week = math.ceil(late_days / 7)
                fine = 0
                for i in range(1, week + 1):
                    if i == week:
                        fine += 10 * math.factorial(i) * (late_days - (week-1) * 7)
                    else:
                        fine += 10 * math.factorial(i) * 7
                self.fine = fine
    def count_book(self):
        count = 0
        for i in books.values():
            if self.name == i.name and self.author == i.author and i.status == "available":
                count += 1
        return count

books = {}

# # Sample data for testing book display
# books = {
#     1001: Book(1001, "Atomic Habits", "James Clear"),
#     1002: Book(1002, "Atomic Habits", "James Clear"),
#     1003: Book(1003, "Deep Work", "Cal Newport"),
#     1004: Book(1004, "Deep Work", "Cal Newport"),
#     1005: Book(1005, "The Alchemist", "Paulo Coelho"),
#     1006: Book(1006, "Clean Code", "Robert C. Martin"),
#     1007: Book(1007, "Clean Code", "Robert C. Martin"),
#     1008: Book(1008, "Ikigai", "Hector Garcia")
# }     

# # Issued but NOT overdue
# books[1001].status = "issued"
# books[1001].issued_by = "Rahul"
# books[1001].issued_roll = "22CS101"
# books[1001].issue_date = dt.datetime.now().date()
# books[1001].return_date = dt.datetime.now().date() + dt.timedelta(days=5)

# # Issued and overdue (~5 days late → week 1)
# books[1003].status = "issued"
# books[1003].issued_by = "Ankit"
# books[1003].issued_roll = "22CS102"
# books[1003].issue_date = dt.datetime.now().date() - dt.timedelta(days=12)
# books[1003].return_date = dt.datetime.now().date() - dt.timedelta(days=5)

# # Issued and overdue (~10 days late → week 2)
# books[1004].status = "issued"
# books[1004].issued_by = "Priya"
# books[1004].issued_roll = "22CS103"
# books[1004].issue_date = dt.datetime.now().date() - dt.timedelta(days=20)
# books[1004].return_date = dt.datetime.now().date() - dt.timedelta(days=10)

# # Issued and overdue (~18 days late → week 3)
# books[1006].status = "issued"
# books[1006].issued_by = "Sneha"
# books[1006].issued_roll = "22CS104"
# books[1006].issue_date = dt.datetime.now().date() - dt.timedelta(days=30)
# books[1006].return_date = dt.datetime.now().date() - dt.timedelta(days=18)