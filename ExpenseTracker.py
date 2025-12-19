from datetime import date, datetime
import matplotlib.pyplot as plt

# ------------------------------------------------------------------
def show_menu():
    menu = """\
    1.   Create an expense
    2.   Remove an expense
    3.   Edit an expense
    4.   Set daily budget
    5.   View all expenses
    6.   Daily total expense
    7.   Show over/under budget
    8.   Graph expenses (Matplotlib)
    9.   Exit
    """
    print(menu)

# ------------------------------------------------------------------

def create_expense(next_id, name, amount, date_str=None, category="uncategorized"):
    if not date_str:
        date_str = date.today().isoformat()

    expense = {
        "id": next_id,
        "name": str(name),
        "amount": float(amount),
        "date": date_str,
        "category": str(category),
    }
    return expense


def remove_entry(expenses_dict):
    if not expenses_dict:
        print("No expenses to remove.")
        return False

    display_all_entries(expenses_dict)
    number = int(input("Enter the ID of the expense you would like to delete: ").strip())

    if number in expenses_dict:
        del expenses_dict[number]
        print(f"Expense #{number} removed.")
        return True
    else:
        print(f"No expense found with id {number}.")
        return False


def edit_entry(expenses_dict):
    if not expenses_dict:
        print("No expenses to edit.")
        return False

    display_all_entries(expenses_dict)
    expense_id = int(input("Which expense would you like to edit? Enter the ID: ").strip())

    if expense_id not in expenses_dict:
        print(f"No expense found with id {expense_id}.")
        return False

    expense = expenses_dict[expense_id]

    change_menu = """\
    1. name
    2. amount
    3. date
    4. category
    """
    print(change_menu)

    change = int(input("Enter the number of the field to edit: ").strip())

    if change == 1:
        expense["name"] = input("Updated name: ").strip()
    elif change == 2:
        expense["amount"] = float(input("Updated amount: ").strip())
    elif change == 3:
        expense["date"] = input("Updated date (YYYY-MM-DD): ").strip()
    elif change == 4:
        expense["category"] = input("Updated category: ").strip()
    else:
        print("Invalid choice.")
        return False

    print(f"Expense #{expense_id} updated.")
    return True


def display_all_entries(expenses_dict):
    if not expenses_dict:
        print("No expenses saved.")
        return

    print("id\tname\tamount\tdate\t\tcategory")
    for eid, e in expenses_dict.items():
        print(f"{eid}\t{e['name']}\t{e['amount']}\t{e['date']}\t{e['category']}")


def daily_total_expense(expenses_dict):
    if not expenses_dict:
        print("No expenses saved.")
        return 0.0

    query_date = input("Enter the date (YYYY-MM-DD): ").strip()
    total = 0.0

    for expense in expenses_dict.values():
        if expense["date"] == query_date:
            total += expense["amount"]

    print(f"Your total expense for {query_date} is: {total}")
    return total


def show_over_under_budget(expenses_dict, daily_budget):
    if not expenses_dict:
        print("No expenses saved.")
        return

    total = daily_total_expense(expenses_dict)

    if total < daily_budget:
        print(f"You are UNDER budget by {daily_budget - total}")
    elif total > daily_budget:
        print(f"You are OVER budget by {total - daily_budget}")
    else:
        print("You spent exactly the budgeted amount.")


def graph_expenses(expenses_dict):
    if not expenses_dict:
        print("No expenses saved.")
        return

    daily_totals = {}

    for expense in expenses_dict.values():
        d = expense["date"]
        daily_totals[d] = daily_totals.get(d, 0) + expense["amount"]

    dates = list(daily_totals.keys())
    totals = list(daily_totals.values())

    plt.figure()
    plt.plot(dates, totals, marker="o")
    plt.xlabel("Date")
    plt.ylabel("Total Spent")
    plt.title("Daily Expenses")
    plt.show()

# ------------------------------------------------------------------
def main():
    expenses = {}
    budget = 0.0
    next_id = 1

    while True:
        show_menu()
        action = int(input("What would you like to do? ").strip())

        if action == 1:
            name = input("Expense name: ").strip()
            amount = float(input("Amount: ").strip())
            date_str = input("Date (YYYY-MM-DD, blank for today): ").strip()
            category = input("Category: ").strip()
            expense = create_expense(next_id, name, amount, date_str, category)
            expenses[next_id] = expense
            next_id += 1
            print("Expense added.")

        elif action == 2:
            remove_entry(expenses)

        elif action == 3:
            edit_entry(expenses)

        elif action == 4:
            budget = float(input("Enter daily budget: ").strip())

        elif action == 5:
            display_all_entries(expenses)

        elif action == 6:
            daily_total_expense(expenses)

        elif action == 7:
            show_over_under_budget(expenses, budget)

        elif action == 8:
            graph_expenses(expenses)

        elif action == 9:
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

main()
