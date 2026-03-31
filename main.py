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
from exceptions import BookNotFoundError

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
    print("|     8) Save library to file                                 |")
    print("|     9) Load library from file                              |")
    print("|     10) Quit Program                                        |")
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


#Function that processes the users answer to the main menu:
def handle_menu_option(choice):
    #Validates choice:
    if choice < 1 or choice > 10:
        print("That is not a valid choice. Please choose a number between 1 and 10")
        return
    #Adds a new book:
    if choice == 1:
        new_book = help_create_book()
        library_inst.add_book(new_book)
        print("The book was succesfully added.")
    #Removes an existing book (add BookNotFoundError):
    elif choice == 2:
        #Gets the books title:
        title = input("What is the title of the book you want to remove ?")
        #If the title input is empty:
        title = title.strip()
        if not title:
            print("Please enter a correct title:")
        #Checks if title exists:
        try:
            library_inst.remove_book(title) #Need to input a title string
            print("The book was succesfully removed")
        except BookNotFoundError:
            print("The title does not exist yet. Please input an elready existing title.")
            return
    elif choice == 3:
        #Gets the books title:
        title = input("What is the title of the book you want to find ?")
        #If the title input is empty:
        title = title.strip()
        if not title:
            print("Please enter a correct title:")
        #Checks if title exists:
        try:
            library_inst.find_book(title)
            print("The book was succesfuly found.")
        except BookNotFoundError:
            print("That title does not exist yet. Please input an already existing title. ")
            return
    #Lists all existing books:
    elif choice == 4:
        library_inst.list_all_books()
    #Lists all read books:
    elif choice == 5:
        library_inst.list_read_books()
    #Lists all unread books:
    elif choice == 6:
        library_inst.list_unread_books()
    #Marks a book as unread or read:
    elif choice == 7:
        #Creates an instance of book:
        bookinst = Book("test", "test", False)
        #Asks the user what it wants to mark it:
        subchoice = input("Do you want this book to be marked as Read (R) or Unread (U) ? Please input either R or U. ")
        #Check if subchoice is empty:
        subchoice = subchoice.strip().lower()
        if not subchoice:
            print("Please input a correct option (R/U):")
        #Gets the books title:
        title = input("What is the title of the book you want to mark ?")
        #If the title input is empty:
        title = title.strip()
        if not title:
            print("Please enter a correct title:")
        #Checks if title exists:
        try:
            library_inst.find_book(title)
        except BookNotFoundError:
            print("That title does not exist yet. Please input an already existing title. ")
            return
        #Determines if subchoice is valid:
        if subchoice in ["r", "read"]:
            bookinst.mark_as_read(title)
        elif subchoice in ["u", "unread"]:
            bookinst.mark_as_unread(title)
        else:
            print("That is not a correct option. Please choose R or U.")
        #Saves the choice to the jsoon file:
        library_inst.save_to_json()                
    #Saves libary to file:
    elif choice == 8:
        library_inst.save_to_json()
    #Loads library from a file:
    elif choice == 9:
        library_inst.load_from_json()
    #Quits the program:
    elif choice == 10:
        return 