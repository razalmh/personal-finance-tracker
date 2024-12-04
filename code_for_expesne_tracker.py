# Global dictionary to store expenses
expenses = {}

def display_menu():
    print("\nExpense Tracker")
    print("1. Add an Expense")
    print("2. View All Expenses")
    print("3. Exit")
    choice = input("Choose an option: ")  # Get user choice
    return choice

def expense_adder():  # Function to add expense
    item = input("Enter the expense item or product: ")
    while True:  # Ensure valid input for money
        value = input("Enter the money spent: ")
        if value.isdigit():
            value = int(value)  # Convert to integer
            break
        else:
            print("Enter a valid number")
    expenses[item] = value  # Add to global dictionary
    print("Expense added:", expenses)  # Display the current state of expenses

def all_expense():  # Function to view all expenses
    if not expenses:  # Check if the dictionary is empty
        print("No expenses recorded.")
    else:
        print("All Expenses:")
        for item, value in expenses.items():  # Loop through dictionary
            print(f"{item}: {value}")

# Main program loop
while True:
    display_menu()  # Show the menu
    choice = display_menu()  # Capture the user choice
    if choice == "1":  # Add expense
        expense_adder()
    elif choice == "2":  # View all expenses
        all_expense()
    elif choice == "3":  # Exit the program
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid input, please try again.")
