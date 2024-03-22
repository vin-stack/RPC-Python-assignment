# models.py

class Book:
    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
