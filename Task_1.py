class BankAccount:
    def __init__(self, name, acc_no, balance):
        self.name = name
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            return "Invalid deposit amount"
        self.balance += amount
        return f"Deposit of {amount:.2f} successful. Current balance is {self.balance:.2f}"

    def withdraw(self, amount):
        if amount <= 0:
            return "Invalid withdrawal amount"
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return f"Withdrawal of {amount:.2f} successful. Current balance is {self.balance:.2f}"

    def display_balance(self):
        return f"Current balance for {self.name} with account number {self.acc_no} is {self.balance:.2f}"

print("Welcome to the bank! Please create your account:") 
name = input("Enter name: ") 
acc_no = input("Enter account number: ") 
while True:
    try:
        balance = float(input("Enter initial balance: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number for the initial balance.")

account = BankAccount(name, acc_no, balance)

while True: 
    print("\nWhat would you like to do?") 
    print("1: Deposit money") 
    print("2: Withdraw money") 
    print("3: Display current balance") 
    print("4: Exit")
    choice = input("Enter choice (1/2/3/4): ")
    print()
    if choice == "1":
        try:
            amount = float(input("Enter amount to deposit: "))
            print(account.deposit(amount))
        except ValueError:
            print("Invalid input. Please enter a valid number for the deposit amount.")
    elif choice == "2":
        try:
            amount = float(input("Enter amount to withdraw: "))
            print(account.withdraw(amount))
        except ValueError:
            print("Invalid input. Please enter a valid number for the withdrawal amount.")
    elif choice == "3":
        print(account.display_balance()) 
    elif choice == "4": 
        print("Thank you for banking with us!")
        break
    else: 
        print("Invalid choice. Please try again.")
