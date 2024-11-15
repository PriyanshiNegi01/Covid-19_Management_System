# Covid-19 Management System

The Covid-19 Management System has a facility to give a unique id for every patient and stores the clinical details of every patient and hospital tests done. This project uses Python in the front-end which is an object-oriented programming language and has connectivity with MYSQL. The Covid-19 Management System can be accessed using a username and password. It is accessible by an administrator or receptionist. Only they can add data into the database. It covers all the required modules right from the patients registration, medicine details, doctor, wards, admin details, bill payment, record modification, discharge details etc.

## Components and Features Used in the Project:

1.	LISTS: A list is a data structure in Python that is mutable (changeable) and represents an ordered sequence of elements. Each element or value inside a list is called an item. Lists are defined using square brackets [ ], with items separated by commas. 

2.	THE IF STATEMENT:  Decision-making is essential when we need to execute specific code only if a certain condition is met. In Python, the if-elif-else statement is used for decision-making. The program evaluates the test expression and executes the statement(s) only if the test expression evaluates to True. If it evaluates to False, the statements are skipped. Python uses indentation to define the body of the if statement. The body starts with an indented block, and the first unindented line marks its end.

3.	THE FOR LOOP: The for loop in Python is used to iterate over a sequence (e.g., list, tuple, string) or other iterable objects. This process, called traversal, allows for repeated execution of a block of code. The for loop also simplifies the management of the loop variable. Using the range() function, you can iterate over a sequence of numbers.

4.	THE WHILE LOOP: The while loop is used to execute a block of statements repeatedly as long as a given condition is True. Once the condition evaluates to False, the program continues with the first line of code after the loop. Python uses indentation to group the statements in the loop, ensuring clarity and consistency.

5.	BREAK AND CONTINUE STATEMENTS: 
•	The break statement allows the program to exit a loop prematurely, skipping any remaining iterations. Execution resumes at the first line following the loop.
•	The continue statement skips the remaining code in the current iteration and jumps to the next iteration of the loop.

6.	NESTED LOOPS: Python supports the use of one loop inside another, known as nested loops. The "inner loop" executes fully for every iteration of the "outer loop," enabling the processing of more complex sequences or structures. 

7.	PYTHON LIBRARY MODULES: A module is a file containing Python code, including statements and definitions. Modules are used to organize large programs into smaller, manageable, and reusable files. By importing a module, we can use its functions and definitions in different programs without redefining them. Python’s standard library is extensive, providing built-in modules for system functionality, file I/O, and standardized solutions for common programming problems.

8.	MySQL DDL COMMANDS: Data Definition Language (DDL) commands are used to define and manage the database schema. These commands handle the structure of database objects and include:
  - CREATE: To create database objects like tables.
  - DROP: To delete database objects.
  - ALTER: To modify existing objects.
  - RENAME: To rename database objects.

9.	MySQL DML COMMANDS: Data Manipulation Language (DML) commands deal with manipulating or modifying data within a database. These commands include:
  - INSERT: To add new records.
  - UPDATE: To modify existing records.
  - DELETE: To remove records.

10.	AGGREGATE FUNCTIONS: Aggregate functions perform calculations on multiple rows of a single column in a table and return a single summarized value. These functions are useful for generating reports or summaries and include: 
  - COUNT: Counts the number of rows.
  - SUM: Calculates the total sum of a column.
  - AVG: Computes the average value.
  - MIN: Finds the minimum value.
  - MAX: Finds the maximum value.

11.	FETCH METHODS:  Python’s cursor class provides methods for retrieving rows from a database:
  - fetchall(): Fetches all rows of a query result and returns them as a list of tuples. An empty list is returned if no rows are found.
  - fetchmany(size): Retrieves the specified number of rows (size) as a list of tuples. Subsequent calls fetch the next set of rows until no more rows are available, at which point an empty list is returned.
  - fetchone(): Returns a single row as a tuple or None if no more rows are available.
  
    Syntax:
    ```
    cursor.fetchall()
    cursor.fetchmany(size)
    cursor.fetchone()
    ```
