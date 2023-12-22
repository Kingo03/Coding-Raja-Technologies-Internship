from typing import List
from main.budget import Expense
import calendar
from datetime import datetime



def main():
    print("Running Expense Tracker!")
    expense_file_path = "expenses.csv"
    budget = 30000
    
    #get user input for expenses!
  #  expense = get_user_expense()
   # print(expense)

    #write their expense to afile.
    #save_expense(expense, expense_file_path)

    #read file and analysis of expenses.
    summarize_expense(expense_file_path, budget)


def get_user_expense():
    print("!Getting User Expense!")
    expense_name = input("Enter Expense name:")
    expense_amount = input("Enter the Expense amount:")
    print("you've entered ",{expense_name} ,{expense_amount}  )

    expense_category = [
          "🍔food",
          "🏠home", 
          "🏢work", 
          "🎉fun",
          "✨misc"
          ]
    while True:
        print("select category:")
        for i, category_name in enumerate(expense_category):
            print(f"{i + 1 }.{category_name}")

        value_range = f"[1 - {len(expense_category)}]"
        selected_index = int(input(f"Enter a category number {value_range}:")) - 1


        if selected_index in range(len(expense_category)):
            selected_category = expense_category[selected_index]
            new_expense = Expense(name=expense_name, category= selected_category , amount = expense_amount)

            return new_expense
        else:
            print("invalid category. pls try valid number for category")



        break
    
    

def save_expense(expense: Expense, expense_file_path):
    print(f"!save User Expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a", encoding="utf-8") as f:
        f.write(f"{expense.name}, {expense.amount}, {expense.category}\n")



def summarize_expense(expense_file_path, budget):
    print("!analyse User Expense!")
    expenses: list[Expense] = []
    with open(expense_file_path, "r", encoding="utf-8") as f:
        lines =f.readlines()
        for line in lines:
            expense_name, expense_amount, expense_category = line.strip().split(",")
            print(expense_name, expense_amount, expense_category)
            line_expense = Expense(
                name=expense_name, amount=expense_amount, category=expense_category
                )
            print(line_expense)
            expenses.append(line_expense)
    print(expenses)       

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount   
    print("expenses by category :")
    for key, amount in amount_by_category.items():
        print(f"{key}: ₹{amount}")   


    
    for i, expense in enumerate(expenses, 1):
       print(f"Expense {i}: Name={expense.name}, Amount={expense.amount}, Type={type(expense.amount)}")


    problematic_amounts = [expense.amount for expense in expenses if not isinstance(expense.amount, (int, float))]
    if problematic_amounts:
        print("Problematic amounts:", problematic_amounts)


    total_spent = sum([float(expense.amount) for expense in expenses])

# Print the results
    print(f"Total spent: ₹{total_spent:.2f} this month!")

    remaining_budget = budget - total_spent
    print(f"Budget remaining: ₹{remaining_budget:.2f}")

    # Get the current date
    current_date = datetime.now()

# Get the last day of the current month
    last_day_of_month = calendar.monthrange(current_date.year, current_date.month)[1]

# Calculate the remaining days in the month
    remaining_days = last_day_of_month - current_date.day

    print(f"Remaining days in the month: {remaining_days}")

    daily_budget = remaining_budget / remaining_days
    print(green(f"budget per day:  ₹{daily_budget:.2f}"))

def green(text):
    return f"\033[92m{text}\033]0m"    





if __name__ =="__main__":
    main()
