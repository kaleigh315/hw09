import unittest
import pandas as pd
class BookLover:
    def __init__(name, email, fav_genre, *args, **kwargs):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = kwargs.get('num_books', None)
        self.book_list = kwargs.get('book_list', None)
    def add_book(self, book_name, rating):
        if isinstance(self.book_list,pd.DataFrame):
            self.rating = rating
            if (self.book_name in self.book_list):
                new_book = pd.DataFrame({'book_name': [book_name],'book_rating': [rating]})
                self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
        else:
            new_book = pd.DataFrame({'book_name': [book_name],'book_rating': [rating]})
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
    def has_read(book_name):
        testValue = test_object.book_name in test_object.book_list.book_name
        return testValue
    def num_books_read(self):
        self.num_books = len(self.book_list)
        return self.num_books
    def fav_books(self):
        self.fav = book_list.query("rating > 3")
        return min(self.fav.book_ratings)
   
    if __name__ == '__main__':
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds", 4)

