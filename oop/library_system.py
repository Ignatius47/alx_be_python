class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.pages = 0
    
class EBook(Book):
        def __init__(self, title, author, file_size):
            super().__init__(title, author)
            self.file_size = file_size

        def __str__(self):
            return f"Title: {self.title}, Author: {self.author}, File Size: {self.file_size} MB"

class PrintBook(Book):
        def __init__(self, title, author, page_count):
            super().__init__(title, author)
            self.page_count = page_count
        
        def __str__(self):
            return f"Title: {self.title}, Author: {self.author}, Page Count: {self.page_count}"

class Library:
        def __init__(self):
         self.books = []

        def add_book(self, book):
            self.books.append(book)

        def list_books(self):
            for book in self.books:
                print(f"Title: {book.title}, Author: {book.author}")