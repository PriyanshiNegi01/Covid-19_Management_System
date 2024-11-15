# Covid-19 Management System

The Covid-19 Management System has a facility to give a unique id for every patient and stores the clinical details of every patient and hospital tests done. This project uses Python in the front-end which is an object-oriented programming language and has connectivity with MYSQL. The Covid-19 Management System can be accessed using a username and password. It is accessible by an administrator or receptionist. Only they can add data into the database. It covers all the required modules right from the patients registration, medicine details, doctor, wards, admin details, bill payment, record modification, discharge details etc.

# Components and Features Used in the Project

### 1. **Lists**
- A list in Python is a mutable (changeable) data structure representing an ordered sequence of elements.  
- Each element inside a list is called an **item**.  
- **Definition**: Lists are defined using square brackets `[ ]`, with items separated by commas.  

---

### 2. **The `if` Statement**
- Decision-making allows for conditional execution of code.  
- **Purpose**: Executes specific statements only if the given condition evaluates to `True`.  
- **Syntax**: Python uses indentation to define the body of the `if` statement, with the body starting at an indented block.  

---

### 3. **The `for` Loop**
- Used to iterate over sequences (e.g., lists, tuples, strings) or other iterable objects.  
- **Process**: Simplifies traversal and loop variable management.  
- **Example**: Use the `range()` function to iterate over a sequence of numbers.

---

### 4. **The `while` Loop**
- Executes a block of code repeatedly as long as a condition is `True`.  
- When the condition evaluates to `False`, the program continues with the code following the loop.  
- **Structure**: Python groups statements inside the loop using indentation for clarity.  

---

### 5. **Break and Continue Statements**
- **`break`**:  
  - Terminates the loop prematurely, skipping remaining iterations.  
  - Execution resumes with the code following the loop.  
- **`continue`**:  
  - Skips the remaining code in the current iteration and moves to the next iteration.

---

### 6. **Nested Loops**
- A loop inside another loop.  
- **Execution**: The inner loop runs fully for every iteration of the outer loop, enabling complex processing.  

---

### 7. **Python Library Modules**
- **Definition**: A module is a file containing Python code, including statements and definitions.  
- **Use**: Organizes large programs into smaller, reusable components.  
- **Advantage**: Access to Python’s extensive standard library for system functionality, file I/O, and common programming tasks.

---

### 8. **MySQL DDL Commands**
Data Definition Language (DDL) commands manage the database schema.  
- **CREATE**: Creates database objects like tables.  
- **DROP**: Deletes database objects.  
- **ALTER**: Modifies existing database objects.  
- **RENAME**: Renames database objects.  

---

### 9. **MySQL DML Commands**
Data Manipulation Language (DML) commands modify or manipulate database data.  
- **INSERT**: Adds new records.  
- **UPDATE**: Modifies existing records.  
- **DELETE**: Removes records.  

---

### 10. **Aggregate Functions**
Perform calculations on multiple rows of a column and return a summarized value:  
- **COUNT**: Counts rows.  
- **SUM**: Calculates the total sum.  
- **AVG**: Computes the average.  
- **MIN**: Finds the minimum value.  
- **MAX**: Finds the maximum value.  

---

### 11. **Fetch Methods**
Python’s cursor class retrieves rows from a database:  
- **`fetchall()`**: Fetches all rows and returns them as a list of tuples.  
- **`fetchmany(size)`**: Retrieves `size` rows as a list of tuples. Returns an empty list if no rows are available.  
- **`fetchone()`**: Returns a single row as a tuple or `None` if no rows are available.  

**Example Syntax**:  
```python
cursor.fetchall()
cursor.fetchmany(size)
cursor.fetchone()
```

