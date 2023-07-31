import statistics
import unittest
import pandas as pd
from booklover import BookLover
class BookLoverTestSuite(unittest.TestCase):
    def test_1_add_book(book, rating): 
        self.book = book
        self.rating = rating
        check_booklist = BookLover('Kaleigh','ear3cg@virginia.edu','fiction')
        check_booklist.add_book(self.book, self.rating)
        self.assertTrue(self.book in check_booklist.book_list)
    def test_2_add_book(book, rating): 
        self.book = book
        self.rating = rating
        check_booklist = BookLover('Kaleigh','ear3cg@virginia.edu','fiction')
        check_booklist.add_book(self.book, self.rating)
        check_booklist.add_book(self.book, self.rating)
        self.assertTrue(check_booklist.book_list.book_name.count(self.book) == 1)
    def test_3_has_read(book): 
        check_read = BookLover('Kaleigh','ear3cg@virginia.edu','fiction')
        check_read.has_read(book)
        self.assertTrue(check_read.testValue)
    def test_4_has_read(book): 
        check_read = BookLover('Kaleigh','ear3cg@virginia.edu','fiction')
        check_read.has_read(book)
        self.assertFalse(check_read.testValue)
    def test_5_num_books_read(book1, book2, book3, rating1, rating2, rating3): 
        num_books_r = BookLover('Kaleigh','ear3cg@virginia.edu','fiction')
        num_books_r.add_book(self.book1, self.rating1)
        num_books_r.add_book(self.book2, self.rating2)
        num_books_r.add_book(self.book3, self.rating3)
        self.assertTrue(num_books_r.num_books == 3)
    def test_6_fav_books(book1, book2, book3, rating1=5, rating2=4, rating3=5): 
        books = BookLover('Kaleigh','ear3cg@virginia.edu','fiction')
        books.add_book(self.book1, self.rating1)
        books.add_book(self.book2, self.rating2)
        books.add_book(self.book3, self.rating3)
        self.assertTrue(books.fav_books > 3)
        
if __name__ == '__main__':
    
    unittest.main(verbosity=3)
