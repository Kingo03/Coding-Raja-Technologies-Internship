
class Expense:
    def __init__(self, name, amount, category):
        self.name = name
        try:
            self.amount = float(amount)
        except ValueError:
            print(f"Warning: Invalid amount for expense '{name}': {amount}")
            self.amount = 0.0  # Set a default value or handle it according to your needs
        self.category = category
