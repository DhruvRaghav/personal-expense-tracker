import os
import platform
import csv

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    print("\n" * 10)  # fallback for VS Code / Jupyter

def add_expense(expenses):
    clear_screen()
    print("Adding an expense...")
    date = input("Enter the date of the expense (YYYY-MM-DD): ")
    try:
        year, month, day = map(int, date.split('-'))
        if not (1 <= month <= 12 and 1 <= day <= 31):
            raise ValueError
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return
    category = input("Enter the category of the expense: ").strip()
    try:
        amount = float(input("Enter the amount of the expense: "))
        if amount < 0:
            raise ValueError
    except ValueError:
        print("Invalid amount. Please enter a positive number.")
        return
    description = input("Enter a description of the expense: ").strip()
    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }
    expenses.append(expense)
    print(f"Expense added: {expense}")
    input("Press Enter to return to menu...")

def view_expenses(expenses):
    clear_screen()
    print("Viewing expenses...")
    if not expenses:
        print("No expenses to view.")
        return
    for idx, exp in enumerate(expenses, 1):
        print(f"Expense {idx}:")
        for k, v in exp.items():
            print(f"{k}: {v}")
        print("--------")
    input("Press Enter to return to menu...")

def budget(expenses):
    clear_screen()

    try:
        total_amount = float(input("Enter the budget for the month: "))
    except ValueError:
        print("Invalid budget input.")
        return
    total_spent = sum(exp.get("amount", 0) for exp in expenses)
    if total_spent > total_amount:
        print("You have exceeded your budget.")
    elif total_spent < total_amount:
        print(f"You have {total_amount - total_spent} left for the month.")
    else:
        print("You have used up your budget exactly!")
    input("Press Enter to return to menu...")

def save_expenses_to_file(expenses, filename="expenses.csv", pause=True):
    clear_screen()
    if not expenses:
        print("No expenses to save.")
        return
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["date", "category", "amount", "description"])
        writer.writeheader()
        writer.writerows(expenses)
    print(f"Expenses saved to {filename}.")
    if pause:
        input("Press Enter to return to menu...")

def load_expenses_from_file(filename="expenses.csv"):
    clear_screen()

    expenses = []
    try:
        with open(filename, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses.append({
                    "date": row["date"],
                    "category": row["category"],
                    "amount": float(row["amount"]),
                    "description": row["description"]
                })
        print(f"{len(expenses)} expenses loaded from {filename}.")
    except FileNotFoundError:
        print(f"No existing {filename} found. Starting fresh.")
    except Exception as e:
        print(f"Error loading expenses: {e}")
    return expenses

def main():
    expenses = load_expenses_from_file()
    while True:
        print("1: Add expense")
        print("2: View expenses")
        print("3: Budget")
        print("4: Save expenses to file")
        print("5: Exit the program")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            budget(expenses)
        elif choice == "4":
            save_expenses_to_file(expenses)
        elif choice == "5":
            print("Exiting the program.")
            save_expenses_to_file(expenses, pause=False)
            print("Thank you for using the expense tracker!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
