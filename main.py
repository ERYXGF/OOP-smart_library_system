"""Entry point and CLI menu loop. Imports from all other files and wires them together.
Instantiates one Library object on startup, loads from json and runs the menu until
the user quits.

    Functions/Objects to write:
    0) Create a library instance that will be used throughout the file.
    1) menu() --> (displays menu/CLI Interface with numbered options)
    2) help_create_book() --> Helper function that prompts user for all book details (title, author, read status) and creates + returns a book object (with input validation)
    3) handle_menu_option(choice) --> Processes user's menu selection: add book, remove book, find book, list all/read/unread books, mark as read/unread, save/load from JSON, exit
    4) main() --> Displays the menu repeatedly in a loop + clears screen between operations + handles error cases + ties everything together

    Error Handling:
    - Catch BookNotFoundError for remove/find operations and display user-friendly messages
    - Handle file I/O errors for save/load operations
    - Validate all user inputs (strings for title/author, boolean for read status, valid menu choices)

Later additional smart features implementation may include: 
Searching books by author, displaying statistics (total books, read percentage), editing book details, confirmation before removing books
"""

#Imports Book and Library class to be used below:
from book import Book
from library import Library

#Creates a library instance that will be used throughout the file: 
library_inst = Library()

#Function that displays the main menu (CLI Interface):
def menu():
    print("|-------------------------------------------------------------|")
    print("|          WELCOME TO THE OOP SMART LIBRARY SYSTEM !          |")
    print("|-------------------------------------------------------------|")
    print("|     1) Add a new book                                       |")                                        
    print("|     2) Remove an existing book                              |")
    print("|     3) Find a book (using its title)                        |")
    print("|     4) List all existing books                              |")
    print("|     5) List all read books                                  |")
    print("|     6) List all unread books                                |")
    print("|     7) Mark a book as read/unread                           |")
    print("|     9) Save library to file                                 |")
    print("|     10) Load library from file                              |")
    print("|     11) Quit Program                                        |")
    print("|_____________________________________________________________|")

#Helper Function that actually creates a book and validates:
def help_create_book():
    while True:
        #Checks if the title is valid:
        answer = input("Please enter the book's title: ")
        answer = answer.strip()
        if not answer:
            print("Please enter the book's title: ")
            continue
        title = answer
        break
    while True:
        #Checks if the author is valid:
        answer2 = input("Please enter the book's author: ")
        answer2 = answer2.strip()
        if not answer2:
            print("Please enter the book's author: ")
            continue
        author = answer2
        break
    while True:
        #Gets the read_status:
        answer3 = input("Do you want to mark this book as read (y) or unread (n) ? ")
        #Checks if it actually contains anything:
        answer3 = answer3.strip().lower()
        if not answer3:
            print("Please enter the book's read_status")
            continue
        #Assigns the read_status:
        if answer3 in ["y", "yes"]:
            read_status = True
        else:
            read_status = False
        break
    book_inst = Book(title, author, read_status)
    return book_inst

