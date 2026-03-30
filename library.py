"""Contains exclusively the Library Class.
This class owns a collection of Book objects stored in a list as an instance attribute. 
Write an add_book() method that receives a Book object and appends it to the collection. 
Write a remove_book() method that finds a book by title and removes it — raise a custom exception if not found. 
Write a find_book() method that searches by title and returns the Book object. 
Write a list_all_books() method that prints all books formatted cleanly. 
Write a list_read_books() and list_unread_books() method. 
Write a save_to_json() and load_from_json() method that uses each Book's to_dict() method to persist and restore the collection. 
Write a __len__ method that returns the number of books in the collection.
"""

#Imports path module to be able to open paths to files:
from pathlib import Path

#Imports json module to be able to load and save to json files:
import json

#Imports the book class:
from book import Book

#Creates the Library Function:
class Library():

    #ATTRIBUTES:
    def __init__(self):
        #Creates an empty list to store book objects:
        self.collection = []

    #METHODS:
    #Receives a book and appends it to the collection:
    def add_book(self, book):
        self.collection.append(book)

    #Finds a book by title abd removes it: raise error if its not found:
    def remove_book(self, title):
        #Searches the books in collection to delete the correct title:
        for book in self.collection:
            if book.title == title:
                self.collection.remove(book)
                return
        #Raises an error if the title isn't found:
        raise Exception(f"Book {title} wasn't found.")

    #Searches for the book title and returns it:
    def search_book(self, title):
        #Searches for the book by title in colection:
        for book in self.collection:
            if book.title == title:
                return book
        #Raise an error if the title isn't found:
        raise Exception(f"Book {title} wasn't found")

    #Prints all books:
    def list_all_books(self):
        #Iterates through collection and prints each book in a formatted way:
        count = 1
        for book in self.collection:
            print(f"{count}) {book}")
            count += 1

    #Returns all read books:
    def list_read_books(self):
        for book in self.collection:
            if book.read_status == True:
                print(book)

    #Returns all unread books:
    def list_unread_books(self):
        for book in self.collection:
            if book.read_status == False:
                print (book)

    #Saves the books to the json file:
    def save_to_json(self):
        #Collect all the books as a dict:
        bookdict = []
        for book in self.collection:
            bookdict.append(book.to_dict())
        #Dumps the bookdict to the json file:
        with open("library.json", "w", encoding = "utf-8") as f:
            json.dump(bookdict, f, indent = 4)

    #Loads the books from the json file:
    def load_from_json(self):
        with open("library.json", "r," encoding = "utf-8") as f:
            json.load(f)

    #Returns how many books are in the collection:
    def __len__(self):
        return len(self.collection)