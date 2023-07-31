import statistics
import unittest
import pandas as pd
from booklover import BookLover
class BookLoverTestSuite(unittest.TestCase):
    def test_1_add_book(self):
        #self.book = book
        #self.rating = rating
        check_booklist = BookLover('Kaleigh','ear3cg@virginia.edu','fiction')
        check_booklist.add_book('The Hunger Games', 5)
        self.assertTrue('The Hunger Games' in check_booklist.book_list['book_name'].values)
    def test_2_add_book(self): 
        #self.book1 = book
        #self.rating1 = rating
        check_booklist = BookLover('Kaleigh','ear3cg@virginia.edu','fiction')
        check_booklist.add_book('It Ends With Us', 5)
        check_booklist.add_book('It Ends With Us', 5)
        self.assertTrue(check_booklist.book_list['book_name'].value_counts()['It Ends With Us']==1)
        #self.assertTrue(check_booklist.book_list['book_name'].count(book) == 1)
    def test_3_has_read(self): 
        #self.book = book
        #self.rating = rating
        check_read = BookLover('Kaleigh','ear3cg@virginia.edu','fiction')
        check_read.add_book('It Ends With Us', 5)
        self.assertTrue(check_read.has_read('It Ends With Us'))
    def test_4_has_read(self): 
        check_read = BookLover('Kaleigh','ear3cg@virginia.edu','fiction')
        self.assertFalse(check_read.has_read('The Hating Game'))
    def test_5_num_books_read(self): 
        #self.book1 = book1
        #self.rating1 = rating1
        #self.book2 = book2
        #self.rating2 = rating2
        #self.book3 = book3
        #self.rating3 = rating3
        num_books_r = BookLover('Kaleigh','ear3cg@virginia.edu','fiction')
        num_books_r.add_book("The Hunger Games", 5)
        num_books_r.add_book("It Ends With Us", 5)
        num_books_r.add_book("Easy", 4)
        self.assertEqual(num_books_r.num_books_read(),3)
    def test_6_fav_books(self,book1="The Hunger Games", book2="It Ends With Us", book3="Easy", rating1=5, rating2=4, rating3=5): 
        books = BookLover('Kaleigh','ear3cg@virginia.edu','fiction')
        books.add_book(book1, rating1)
        books.add_book(book2, rating2)
        books.add_book(book3, rating3)
        self.assertTrue(books.fav_books() > 3)
        
if __name__ == '__main__':
    
    unittest.main(verbosity=3)
