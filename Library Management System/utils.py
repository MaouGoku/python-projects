# Main Data Storage
import datetime as dt
import random as rd

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




        