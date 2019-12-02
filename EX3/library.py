# coding: utf8

class Library():

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)


    def get_book(self, title):
        for book in self.books:
            if title == book.title:
                return book
        raise Exception("le titre n'est pas dans la Library")
