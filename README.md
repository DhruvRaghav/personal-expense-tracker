# Personal Expense Tracker

## Description

The **Personal Expense Tracker** is a command-line Python application that allows users to:

- Log, view, and manage daily expenses
- Track monthly spending habits
- Set and compare against a predefined monthly budget
- Persist and reload expenses using CSV files

Users can continue from where they left off by automatically loading saved data at program startup.

---

## Features

- **Add Expense**:  
  Enter the date, category, amount, and description. Includes input validation.

- **View Expenses**:  
  Lists all expenses in a readable format.

- **Set Budget**:  
  Compares user-defined monthly budget to actual expenses.

- **Save to CSV**:  
  Stores current expenses to a `Project.csv` file.

- **Load from CSV**:  
  Automatically loads saved data from `Project.csv` at startup.

---

## File Structure
project-directory/
│
├── budget.py # Main application script
├── Project.csv # CSV file storing all expenses
└── README.md # Project documentation



---

## Sample Expense Format (CSV)

```csv
- date,category,amount,description
- 2024-07-01,food,10.5,Lunch at cafeteria
- 2024-07-02,transport,3.0,Bus fare


## How to Run
- Make sure Python 3 is installed on your system.

- Then run the application using the terminal:t
python budget.py





## Limitations & Future Enhancements
- Only CSV used for storage (future: SQLite or JSON)
- No GUI (consider Tkinter or Flask-based UI)
- Expense categories are free text (can be standardized via dropdown/list)

## Conclusion
- This project highlights how Python’s basic file I/O, data validation, and user interaction can address real-world problems. It provides a foundation for expanding into more advanced personal finance and data analytics tools.



