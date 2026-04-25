# Main Data Storage
import datetime as dt
import math

books = {}
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




        