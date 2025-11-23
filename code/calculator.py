expenses = []   # list to store data

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    expenses.append({"name": name, "amount": amount})
    print("\nExpense added successfully!")

def view_expenses():
    print("\n---- All Expenses ----")
    for i, e in enumerate(expenses, 1):
        print(f"{i}. {e['name']} - ₹{e['amount']}")
    print("------------------------")

def delete_expense():
    view_expenses()
    n = int(input("Enter expense number to delete: "))
    if 0 < n <= len(expenses):
        del expenses[n-1]
        print("\nExpense deleted successfully!")
    else:
        print("Invalid number!")

def show_summary():
    total = sum(e["amount"] for e in expenses)
    print(f"\nTotal Expenses = ₹{total}")

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. View Summary")
    print("5. Exit")

    choice = input("Choose (1-5): ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        delete_expense()
    elif choice == "4":
        show_summary()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.")
