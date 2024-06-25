import time
accounts = {}



def create_account():
    account_number = input("Enter your account number: ")
    account_name = input("Enter your username: ")
    
    while account_name.isdigit():
        print("Invalid input, no numbers allowed in the username.")
        account_name = input("Enter your username: ")
    
    account_password = input("Enter your password: ")
    
    balance = input("Enter your balance: ")
    while not balance.isdigit():
        print("Please enter a valid number for the balance.")
        balance = input("Enter your balance: ")
    
    balance = int(balance)
    accounts[account_number] = {
        "account_name": account_name,
        "password": account_password,
        "balance": balance,
    }
    
    print(f"Your username is {account_name}, your password is {account_password}, and your account balance is ${balance}.")

def deposit():
    account_number = input("Enter your account number: ")
    
    while account_number not in accounts:
        print("Account not found. Try again.!!!")
        account_number = input("Enter your account number: ")
    
    print("You are logged in.")
    deposit_amount = input("Enter the amount you want to deposit: ")
    
    while not deposit_amount.isdigit():
        print("Please enter a valid number for the deposit amount.")
        deposit_amount = input("Enter the amount you want to deposit: ")
    
    deposit_amount = int(deposit_amount)
    accounts[account_number]["balance"] += deposit_amount
    print(f"Your deposit is {deposit_amount} and Your current balance is ${accounts[account_number]['balance']}.")




def withdraw():
    account_number = input("Enter your account number here: ")
    while account_number not in accounts:
        print("Account not found.Try again!!!")
        account_number = input("Enter your account number here: ")
    
    print("You are logged in.")
    withdraw_amount = input("Enter the amount you want to withdraw: ")
    while not withdraw_amount.isdigit():
        print("Please enter valid number for the deposit amount.")
        withdraw_amount = input("Enter the amount you want to withdraw: ")

    withdraw_amount = int(withdraw_amount)
    accounts[account_number]["balance"] -= withdraw_amount
    print(f"Your withdraw is {withdraw_amount} and you current balance is ${accounts[account_number]["balance"]}")




def check_balance():
    account_number = input("Enter your account number here: ")
    while account_number not in accounts:
        print("Account not found.Try again!!!")
        account_number = input("Enter your account number here: ")
    print(f"Your balance is ${accounts[account_number]["balance"]}")




def main_menu():
    while True:
        print("\nWelcome to atuka's Bank")
        print("0. Create account")
        print("1. Check balance")
        print("2. Deposit")
        print("3. withdraw")
        print("4. Exit")



        option = input("Enter choice: ")


        if option == "0":
            create_account()
        elif option == "1":
            check_balance()
        elif option == "2":
            deposit()
        elif option == "3":
            withdraw()
        elif option == "4":
            print("Thanks for using atuka's bank")
            break
        else:
            print("Invalid option!!!")





def connect():
    print("Connecting to the atuka's Bank...")
    time.sleep(3)
    print("You are connected to atuka's Bank!!!")




connect()
main_menu()






