import unittest
import pandas as pd
class BookLover:
    def __init__(self, name, email, fav_genre, num_books = 0, book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list
    def add_book(self, book_name, rating):
        #self.book_name = book_name
        #self.rating = rating
        if (book_name in self.book_list['book_name'].values):
            pass
        else:
            new_book = pd.DataFrame({'book_name': [book_name],'book_rating': [rating]})
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
        return self.book_list
    def has_read(self,book_nme):
        #self.book_name = book_name
        boolean = (book_nme in self.book_list['book_name'].values)
        return (boolean)
    def num_books_read(self):
        num_books = len(self.book_list)
        return num_books
    def fav_books(self):
        fav = self.book_list.query("book_rating > 3")
        return min(fav['book_rating'].values)
'''   
if __name__ == '__main__':
        
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds", 4)
'''
