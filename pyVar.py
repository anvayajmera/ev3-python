class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")

    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: ${self.balance}"




def bank_system():
    accounts = {}

    while True:
        print("Bank System")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Quit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '5':
            print("Exiting bank system.")
            break

        if choice == '1':
            name = input("Enter account owner's name: ")
            accounts[name] = Account(name)
            print(f"Account created for {name}.")

        elif choice in ('2', '3', '4'):
            name = input("Enter account owner's name: ")

            if name not in accounts:
                print("Account not found.")
                continue

            account = accounts[name]

            if choice == '2':
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            elif choice == '3':
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            elif choice == '4':
                print(account)
        else:
            print("Invalid input. Please try again.")

bank_system()
