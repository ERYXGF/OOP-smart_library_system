"""This file contains exclusively the book class. Every book has a title, author, year of publication, genre and a read status that starts as False by default. 
The __init__ method receives all these as parameters except read status which is always initialised to False. 
Write a mark_as_read() method that sets the status to True and records the date it was marked using datetime. 
Write a mark_as_unread() method that resets it. 
Write a __str__ method that returns a clean formatted single-line summary of the book. 
Write a __repr__ method that returns a more technical representation. 
Write a to_dict() method that converts the book's attributes to a dictionary — you'll use this for JSON saving."""

#imports datetime to be used in the mark_as_read method:
import datetime

#Creates the book class:
class Book():

    #ATTRIBUTES:
    #Init attribute:
    def __init__(self, title, author, publication_date, genre, read_status = False):
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.genre = genre
        self.read_status = read_status

    #METHODS:
    #Marks the book as read and returns the time:
    def mark_as_read(self):
        self.read_status = True
        return self.read_status, datetime.datetime.now()
    #Marks the book as unread and returns the time:
    def mark_as_unread(self):
        self.read_status = False
        return self.read_status, datetime.datetime.now()
    #Returns a one-line summary of the book:
    def __str__(self):
        return f"{self.title} by {self.author} in {self.publication_date} is from the {self.genre} genre."
    #Returns a technical representation of the book:
    def __repr__(self):
        return f"title= {self.title}, author= {self.author}, publication_date= {self.publication_date}, genre= {self.genre}, read_status= {self.read_status}"
    #Converts the book's infos to a dictionnary so that it can be stored in a json file:
    def to_dict(self):
        return {
            "title" : self.title, 
            "author" : self.author, 
            "publication_date" : self.publication_date, 
            "genre" : self.genre, 
            "read_status" : self.read_status
    }