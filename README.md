# python-Advance-projects
# 1. DICE SEMULATION
Working of the Game:
I am using the time module and random module in this project. The game operates within two while loops:

First Loop:
Controls whether the player wants to play the game or exit.
Second Loop:
Handles the actual gameplay.
The first turn is always for the user.
The second turn is for the computer, which makes random moves using the random module.
Additional Features:
I am using user-defined functions to manage different parts of the game efficiently.
Only the user can stop the game by giving a command—the computer will never stop on its own.
This makes the game more interactive and engaging, providing an interesting experience for the player.
# 2. HOTEL MANAGEMENT SYSTEM

my project is a real-life Café Management System that uses Python and MySQL with the mysql.connector module. It interacts with a MySQL database to store and manage the café's menu, allowing customers to place orders and generate bills.

How It Works:
1.The system performs SQL queries to fetch, insert, create, and delete data from the MySQL database.
2.It provides a user-friendly interface with logical loops and conditions to handle the order-taking process efficiently.
3.Customers can view the menu, place orders, confirm orders, and generate bills dynamically.
4.The system calculates the total bill based on selected items and their prices from the database.
5.It simulates a real café environment, where waiters (referred to as "better" in the program) take orders and process payments.

# 3. LIBRARY MANAGEMENT SYSTEM
--->working: This Python script implements a Library Management System that allows three types of users—teachers, students, and administrators—to log in and perform various tasks related to books. The system interacts with a MySQL database using the mysql.connector library and utilizes bcrypt for password hashing and authentication.
Main Components & Functionality:
1. User Authentication & Role-Based Access. 2. Teacher Login & Operations. 3. Student Login & Operations. 4. Admin Login & Privileges. 5. Database Connectivity & Queries
# 4. contact app 
Working of the Contact Diary App
The Contact Diary App is a Python-based application that allows users to store, search, count, and delete contacts using a MySQL database. It provides a menu-driven interface for easy interaction and ensures that contacts are securely stored and managed.

1️⃣ Database Connection and Table Creation
The app first establishes a connection with a MySQL database (library_system) using the mysql.connector module. If the contact table does not exist, it is created with three fields:

name (VARCHAR)
email (VARCHAR)
phone (VARCHAR, used as the primary key to prevent duplicate contacts)
2️⃣ Menu-Driven Interface
The program runs in a loop, continuously displaying the menu until the user chooses to exit. The menu provides six main functionalities:

Create Contact

The user enters a name, email, and phone number.
The details are inserted into the MySQL database.
If the contact is successfully added, a confirmation message is displayed.
Search Contact

The user can search by name or phone number.
The app retrieves and displays the contact details if found.
If the contact does not exist, an error message is shown.
Count Contacts

The app counts and displays the total number of contacts stored in the database.
Delete a Single Contact

The user can delete a contact by name or phone number.
If the contact exists, it is removed from the database.
If the contact is not found, an error message is shown.
Delete All Contacts

The user is asked for confirmation before deleting all contacts.
If confirmed, all records in the contact table are erased.
Exit the Application

The app ensures that all changes are saved before closing the database connection.
3️⃣ Error Handling & Optimization
Input Validation: Ensures that inputs are properly formatted.
Database Commit: Saves changes after each modification.
Efficient Query Execution: Uses fetchone(), fetchall(), and rowcount to optimize search and deletion.
Structured and Readable Code: Functions are well-organized for easy maintenance.

