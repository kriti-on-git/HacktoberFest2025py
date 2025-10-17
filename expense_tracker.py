import json
import os
from datetime import datetime

DATA_FILE = "expenses.json"

def load_expenses():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_expenses(expenses):
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=4)

def add_expense():
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category: ").strip()
        date_str = input("Enter date (YYYY-MM-DD) or leave blank for today: ").strip()
        date = date_str if date_str else datetime.today().strftime("%Y-%m-%d")
        
        expenses = load_expenses()
        expenses.append({"amount": amount, "category": category, "date": date})
        save_expenses(expenses)
        print("Expense added.")
    except ValueError:
        print("Invalid amount. Try again.")

def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded.")
        return
    print("\n--- Expenses ---")
    total = 0
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. {exp['date']} - {exp['category']} - ${exp['amount']:.2f}")
        total += exp['amount']
    print(f"Total spent: ${total:.2f}")

def delete_expense():
    expenses = load_expenses()
    if not expenses:
        print("No expenses to delete.")
        return
    view_expenses()
    try:
        idx = int(input("Enter the number of the expense to delete: "))
        if 1 <= idx <= len(expenses):
            removed = expenses.pop(idx - 1)
            save_expenses(expenses)
            print(f"Removed expense: {removed['category']} - ${removed['amount']:.2f}")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
