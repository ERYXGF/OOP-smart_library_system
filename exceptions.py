"""Contains all custom exceptions classes for the project. 
Only 1 exception is needed: BookNotFoundError
"""

#Creates the error class:
class BookNotFoundError(Exception): #Inherits from Python's own exception class
    pass
"""By inheriting from Python's exception class, this class basically doesn't need
to do anything apart from exist and be called"""