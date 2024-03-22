# book.py

class Book:
    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

class BookManager:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.books.append(book)

    def update_book(self, isbn, title=None, author=None):
        for book in self.books:
            if book.isbn == isbn:
                if title:
                    book.title = title
                if author:
                    book.author = author
                return True
        return False

    def delete_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                return True
        return False

    def list_books(self):
        if not self.books:
            print("No books available.")
        else:
            for book in self.books:
                availability = "Available" if book.available else "Not Available"
                print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Availability: {availability}")

    def search_book_by_title(self, title):
        found_books = [book for book in self.books if book.title.lower() == title.lower()]
        return found_books

    def search_book_by_author(self, author):
        found_books = [book for book in self.books if book.author.lower() == author.lower()]
        return found_books

    def search_book_by_isbn(self, isbn):
        found_books = [book for book in self.books if book.isbn == isbn]
        return found_books

    def check_out_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and book.available:
                book.available = False
                return True
        return False

    def check_in_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and not book.available:
                book.available = True
                return True
        return False
