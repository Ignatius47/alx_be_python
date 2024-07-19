class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = publication_year

    def __del__(self):
        print(f"Deleting: {self.title}")

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Publication Year: {self.year}"
    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', year={self.year})"
