# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 18:40:29 2023

@author: Sashwath
"""

class Bookshelf:
    def __init__ (self,name,author,book_price,published_in):
        self.name_of_the_book = name
        self.author_of_the_book = author
        self.book_price_of_the_book = book_price
        self.published_in = published_in

    def add_book(self):
        print("Name: "+self.name_of_the_book)
        print("Author: "+self.author_of_the_book)
        print("Book_Price: "+self.book_price_of_the_book)
        print("Published_In: "+self.published_in)
        print("Book Added \n")


book1 = Bookshelf("Harry Potter and the Philospoher's Stone","J.K Rowling","1928","1997")
book1.add_book()
print("The book was published in the year of 1997")

book2 = Bookshelf("Diary of a Wimpy Kid","Jeff Kinney","700","2017")
book2.add_book()
print("The book was published in the year of 2017")