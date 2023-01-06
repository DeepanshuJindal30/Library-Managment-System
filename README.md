# Library-Managment-System

This code is a Python script that contains functions related to a library management system. It appears to allow a user to select and lend a book from a library database.

The **mysql.connector** library is imported, which allows the script to connect to a MySQL database.

The **user_choice** function prompts the user to enter the name of a book and returns their input as a string.

The **check_quntity** function takes a book name as input and checks the quantity of that book in the library database. It returns a boolean value indicating whether the quantity is greater than or equal to 1.

The **show_book** function takes a type of book as input and returns a list of tuples, where each tuple contains the name of a book of the specified type from the library database.

The **select_ask** function presents the user with options to either try again or redirect to the lend book function.

The **update** function updates the book a user has borrowed in the library database and decreases the quantity of the borrowed book by 1. If the Task input is 1, the function increases the quantity of the returned book by 1 instead.

The **your_id** function returns the latest user ID from the library database as an integer.

The **select** function presents the user with options to either choose a book from a list or search for a specific book. If the user chooses a book from the list, the function checks if the book is available and updates the database if it is. If the user searches for a specific book, the function checks if the book is available and updates the database if it is.



