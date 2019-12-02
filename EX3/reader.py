# coding: utf8

class Reader():
    """"""
    def __init__(self):
        self.book = None

    def borrow_book(self,library,title):
        try:
            self.book = library.get_book(title)
        except Exception as e:
            print(e)

    def go_to_page(self,page_number):

        pass

    def next_page(self):
        """"""
        pass

    def previous_page(self):
        """"""
        pass

    def read(self):
        """"""
        pass

    def read_book(self):
        """"""
        pass
