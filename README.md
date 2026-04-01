<span style="color:purple">OOP Smart Library System</span> 📚
A <span style="color:blue">command-line interface (CLI)</span> application built with <span style="color:green">Python's object-oriented programming (OOP)</span> principles to manage a personal library of books. Users can add, remove, find, and organize books, with features like marking read/unread status and persisting data to JSON files. 🚀

<span style="color:orange">Features</span> ✨
<span style="color:red">Add Books</span>: Create new book entries with title, author, and read status. ➕
<span style="color:red">Remove Books</span>: Delete books by title with error handling for non-existent titles. 🗑️
<span style="color:red">Find Books</span>: Search for books by title and display details. 🔍
<span style="color:red">List Books</span>: View all books, or filter by read/unread status. 📋
<span style="color:red">Mark Read/Unread</span>: Update a book's read status and save changes. ✅
<span style="color:red">Persistence</span>: Save and load the library from a JSON file (library.json). 💾
<span style="color:red">Input Validation</span>: Robust validation for all user inputs to prevent errors. 🛡️
<span style="color:red">Error Handling</span>: Custom exceptions for book not found scenarios. ⚠️
<span style="color:red">CLI Interface</span>: User-friendly menu-driven interface with screen clearing between operations. 🖥️
<span style="color:teal">Installation</span> 🔧
<span style="color:navy">Prerequisites</span>:

Python 3.6 or higher installed on your system. 🐍
<span style="color:navy">Clone or Download</span>:

Download the project files to a local directory. 📥
<span style="color:navy">Run the Application</span>:

Open a terminal in the project directory. 💻
Execute: python main.py ▶️
No external dependencies are required beyond Python's standard library. 🎉

<span style="color:magenta">Usage</span> 📖
<span style="color:olive">Start the Program</span>:

Run python main.py to launch the CLI menu. 🚀
<span style="color:olive">Navigate the Menu</span>:

Choose options 1-10 as displayed. 🔢
Follow prompts for inputs (e.g., book details, titles). ✏️
<span style="color:olive">Example Workflow</span>:

Add a book (Option 1): Enter title, author, and read status. ➕
List all books (Option 4): View formatted list. 📋
Mark a book as read (Option 7): Select book and update status. ✅
Save to file (Option 8): Persist changes to library.json. 💾
Quit (Option 10): Exit with a goodbye message. 👋
<span style="color:olive">Data Persistence</span>:

Library data is automatically saved to library.json on relevant operations. 💾
Load existing data on startup if the file exists. 🔄
<span style="color:silver">Project Structure</span> 🏗️
book.py: Defines the Book class with attributes (title, author, publication date, genre, read status) and methods (mark as read/unread, to_dict for JSON). 📖
exceptions.py: Contains custom exception BookNotFoundError for error handling. 🚨
library.py: Implements the Library class to manage a collection of books, with methods for add, remove, find, list, save/load JSON. 📚
main.py: Entry point with CLI menu, input handling, and main loop. 🎯
README.md: This documentation file. 📄
LICENSE: Project license information. 📜
<span style="color:maroon">Error Handling</span> ⚠️
<span style="color:crimson">BookNotFoundError</span>: Raised when attempting to remove or find a non-existent book. 🚫
<span style="color:crimson">Input Validation</span>: Checks for empty strings, invalid ranges, and type mismatches. ✅
<span style="color:crimson">File I/O</span>: Graceful handling of JSON load/save errors. 💾
<span style="color:gold">Contributing</span> 🤝
Contributions are welcome! To contribute:

Fork the repository. 🍴
Create a feature branch. 🌿
Make changes and test thoroughly. 🧪
Submit a pull request with a description of changes. 📤
<span style="color:violet">License</span> 📜
This project is licensed under the MIT License. See LICENSE for details. 🆓

<span style="color:indigo">Future Enhancements</span> 🔮
Search by author or genre. 🔍
Display library statistics (total books, read percentage). 📊
Edit book details. ✏️
Confirmation prompts for destructive actions (e.g., remove). ❓
GUI version using Tkinter or web interface with Flask. 🌐
