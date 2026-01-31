import csv
from datetime import datetime

FILE_NAME = "expenses.csv"

def validate_amount(value):
    try:
        amount = float(value)
        if amount <= 0:
            raise ValueError
        return amount
    except ValueError:
        print("Invalid amount. Enter a positive number.")
        return None


def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return date_str
    except ValueError:
        print("Date format must be YYYY-MM-DD")
        return None

def initialize_file():
    try:
        with open(FILE_NAME, "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["date", "category", "amount", "note"])
    except FileExistsError:
        pass

def add_expense():
    date = None
    while not date:
        date = validate_date(input("Enter date (YYYY-MM-DD): "))

    category = input("Enter category (Food, Travel, Shopping, etc): ").strip()

    amount = None
    while not amount:
        amount = validate_amount(input("Enter amount: "))

    note = input("Enter note (optional): ").strip()

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, note])

    print("Expense added successfully!")

def read_expenses():
    expenses = []
    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["amount"] = float(row["amount"])
            expenses.append(row)
    return expenses

def show_summary():
    expenses = read_expenses()
    total = sum(exp["amount"] for exp in expenses)
    print(f"\nTotal Expenses: ₹{total:.2f}")


def category_wise_summary():
    expenses = read_expenses()
    category_total = {}

    for exp in expenses:
        category = exp["category"]
        category_total[category] = category_total.get(category, 0) + exp["amount"]

    print("\nCategory-wise Summary:")
    for cat, amt in category_total.items():
        print(f"{cat}: ₹{amt:.2f}")

def delete_expense():
    expenses = read_expenses()

    if not expenses:
        print("No expenses to delete.")
        return

    print("\n🗑Expense List:")
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. {exp['date']} | {exp['category']} | ₹{exp['amount']} | {exp['note']}")

    try:
        choice = int(input("\nEnter expense number to delete: "))
        if choice < 1 or choice > len(expenses):
            raise ValueError
    except ValueError:
        print("Invalid choice.")
        return

  

def export_report():
    expenses = read_expenses()

    with open("report.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["date", "category", "amount", "note"])
        writer.writeheader()
        writer.writerows(expenses)

    print("Report exported as report.csv")

def main():
    initialize_file()

    while True:
        print("""
====== Expense Tracker ======
1. Add Expense
2. Show Total Summary
3. Category-wise Summary
4. Export Report
5. Delete Expense
6. Exit
""")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            show_summary()
        elif choice == "3":
            category_wise_summary()
        elif choice == "4":
            export_report()
        elif choice == "5":
            delete_expense()
        elif choice == "6":
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()