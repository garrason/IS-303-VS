# Store each valid expense in a list.
expenses = []

print("Personal Expense Analyzer")
print("Enter 0 when you are finished entering expenses.")

# Gather expenses until the user enters 0.
while True:
    expense = float(input("Enter an expense or 0 to finish: "))

    if expense == 0:
        break
    elif expense < 0:
        print("Expenses cannot be negative. Please try again.")
    else:
        expenses.append(expense)

# Analyze the list only if at least one expense was entered.
if len(expenses) == 0:
    print("No expenses were entered.")
else:
    small_count = 0
    moderate_count = 0
    large_count = 0

    # Count the number of small, moderate, and large expenses
    for expense in expenses:
        if expense < 25:
            small_count += 1
        elif expense <= 100:
            moderate_count += 1
        else:
            large_count += 1

    # Calculate the expense summary
    expense_count = len(expenses)
    total_expenses = sum(expenses)
    average_expense = total_expenses / expense_count
    smallest_expense = min(expenses)
    largest_expense = max(expenses)

    # Print the summary and format the dollar amounts
    print("Expense Summary")
    print("---------------")
    print(f"Number of expenses: {expense_count}")
    print(f"Total: ${total_expenses:,.2f}")
    print(f"Average: ${average_expense:,.2f}")
    print(f"Smallest expense: ${smallest_expense:,.2f}")
    print(f"Largest expense: ${largest_expense:,.2f}")
    print()
    print(f"Small expenses: {small_count}")
    print(f"Moderate expenses: {moderate_count}")
    print(f"Large expenses: {large_count}")
