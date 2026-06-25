class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    def show_balance(self):
        print("Current Balance:", self.balance)

account = BankAccount(1000)

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        account.deposit(int(input("Enter amount: ")))
    elif choice == "2":
        account.withdraw(int(input("Enter amount: ")))
    elif choice == "3":
        account.show_balance()
    elif choice == "4":
        print("Thank You!")
        break
    else:
        print("Invalid Choice")

 output:       



1. Deposit
2. Withdraw
3. Show Balance
4. Exit
Enter choice: 2
Enter amount: 4500
Insufficient Balance

1. Deposit
2. Withdraw
3. Show Balance
4. Exit
Enter choice: 1
Enter amount: 5000
Deposited: 5000

1. Deposit
2. Withdraw
3. Show Balance
4. Exit
Enter choice: 3
Current Balance: 6000
