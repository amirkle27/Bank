from datetime import datetime
from datetime import datetime
date_format = "%Y-%m-%d"


bank_accounts = {
    1001: {
        "first_name": "Alice",
        "last_name": "Smith",
        "id_number": "123456789",
        "balance": 2500.50,
        "transactions_to_execute": [
            ("2024-08-26 14:00:00", 1001, 1002, 300), ("2024-08-26 15:00:00", 1001, 1003, 200), ("2024-08-26 10:00:00", 1001, 1003, 200)],
        "transaction_history": [
            ("2024-08-15 09:00:00", 1001, 1002, 500, "2024-08-15 09:30:00", 1001, 1002, 1000)]
    },
    1002: {
        "first_name": "Bob",
        "last_name": "Johnson",
        "id_number": "987654321",
        "balance": -3900.75,
        "transactions_to_execute": [("2025-01-23 10:05:00", 1002, 1001, 3000), ("2025-08-17 15:00:00", 1002, 1003, 2000)],
        "transaction_history": [("2024-08-25 09:00:00", 1002, 1004, 500, "2024-08-15 09:30:00", 1002, 1004, 1000)]

    },
    1003: {
        "first_name": "Charles",
        "last_name": "Bronson",
        "id_number": "222014651",
        "balance": -40000000.4,
        "transactions_to_execute": [("2024-09-06 10:05:00", 1003, 1001, 30000), ("2025-02-23 15:00:00", 1003, 1004, 400)],
        "transaction_history": [("2022-01-23 10:05:00", 1003, 1001, 30000), ("2022-02-23 15:00:00", 1003, 1002, 400)]
    },
    1004:{
        "first_name": "Arnon",
        "last_name": "Zadok",
        "id_number": "323395176",
        "balance": -50000,
        "transactions_to_execute": [("2025-07-11 12:00:00", 1004, 1001, 30), ("2025-09-15 10:00:00", 1004, 1003, 15)],
        "transaction_history": [("2024-08-25 14:00:00", 1004, 1002, 1500), ("2001-01-28 12:07:00", 1004, 1002, 9200)]
        }
    }
sample_account = {
    "first_name": " ",
    "last_name": " ",
    "id_number": " ",
    "balance": 000,
    "transactions_to_execute": [
        ("%Y-%m-%d %H:%M:%S", 0000, 0000, 000), ("%Y-%m-%d %H:%M:%S", 0000, 0000, 000)],
    "transaction_history": [
        ("%Y-%m-%d %H:%M:%S", 0000, 0000, 000, "%Y-%m-%d %H:%M:%S", 0000, 0000, 000)]
}

def printing_accounts (bank_accounts):
    for account_number, details in bank_accounts.items():
        print(f"Account Number: {account_number}")
        for key, value in details.items():
            print(f"{key.capitalize()}: {value}")
        print(f"-" *100 + "\n")

def account_by_number ():
    account_number = int(input("Which Account would you Like to Display? "))
    access_details = bank_accounts.get(account_number)
    print("\n")
    print(f"Account Number: {account_number}")
    for key, value in access_details.items():
        print(f"{key.capitalize()}: {value}")
    print("\n")

def account_by_id():
    id_number = input("Please enter the ID number: ").strip()
    accounts_found = []
    for account_number, details in bank_accounts.items():
        if details['id_number'] == id_number:
            accounts_found.append((account_number, details))
    if accounts_found:
        print(f"\nAccounts found for ID {id_number}:")
        for account_number, access_details in accounts_found:
            print("\n")
            print(f"Account Number: {account_number}")
            for key, value in access_details.items():
                print(f"{key.capitalize()}: {value}")
            print("\n")
    else:
        print(f"\nNo accounts found for ID {id_number}.\n")

def account_by_name ():
    first_name = input("Please Enter Client's First Name: ").lower().strip()
    accounts_found = []
    for account_number, details in bank_accounts.items():
        if details ['first_name'].lower() == first_name:
            accounts_found.append((account_number,details))
    if accounts_found:
        print(f"\nAccounts Found for First Name: {first_name}\n")
        for account_number, details in accounts_found:
            print(f"Account Number: {account_number}")
            for key, value in details.items():
                print(f"{key.capitalize()}: {value}")
            print("\n" + "-" * 100 + "\n")
    else:
            print(f"\nNo accounts found for first name: {first_name}\n")

def sorted_by_balance():
    sorted_accounts = (dict(sorted(bank_accounts.items(), key = lambda bank_accounts: bank_accounts[1]['balance'])))
    for account_number, details in sorted_accounts.items():
        print("Displaying all Accounts Sorted by Balance")
        for key, value in details.items():
            print(f"{key.capitalize()}: {value}")
        print(f"-" *100 + "\n")

def history_transactions_sorted():
    sorted_accounts = (dict(sorted(bank_accounts.items(), key = lambda bank_accounts: bank_accounts[1]['transaction_history'])))
    for account_number, details in sorted_accounts.items():
        print("Displaying all Transactions Sorted by Time of Transaction")
        for key, value in details.items():
            print(f"{key.capitalize()}: {value}")
        print(f"-"* 100 + "\n")

def today_transactions():
    today = datetime.today().date()  # Get today's date
    today_transactions = {
        account_number: details for account_number, details in bank_accounts.items()
        if any(datetime.strptime(txn[0], "%Y-%m-%d %H:%M:%S").date() == today for txn in
               details['transactions_to_execute'])
    }
    if today_transactions:
        print("Transactions scheduled for today:")
        for account_number, details in today_transactions.items():
            print(f"\nAccount Number: {account_number}")
            for txn in details['transactions_to_execute']:
                if datetime.strptime(txn[0], "%Y-%m-%d %H:%M:%S").date() == today:
                    print(f"Transaction: {txn}")
            print("-" * 100 + "\n")
    else:
        print("\nNo transactions scheduled for today.\n")

def negative_balance ():
    negative = filter(lambda bank_accounts: bank_accounts[1]['balance']<0, bank_accounts.items())
    negative_sorted = sorted(negative,key= lambda bank_accounts: bank_accounts[1]['balance'], reverse=True)
    negative_sorted_dict = dict(negative_sorted)
    for account_number, details in negative_sorted_dict.items():
        print("\nAccounts with Negative Balance: \n")
        for key, value in details.items():
            print(f"{key}: {value}")
        print("-"*100 + "\n")

def all_balances ():
    total_balance = []
    for account_number, details in bank_accounts.items():
        total_balance.append(details['balance'])
    print (f"\nTotal Balance from all Accounts is: {sum(total_balance)}\n")

def main_menu ():
    while True:
        operation: str = str(input(F"Hello, which operation would you like to perform? \nOpen an New Account [N] \nWork on an Existing Account [E] \nSee Bank Reports [R]\nQuit [Q]"))
        if operation.lower() == "n":
            try:
                print("Starting a new account creation process:")
                new_account_number: int = int(max(bank_accounts.keys())+1)
                new_account = sample_account.copy()
                new_account.update({
                "first_name" :  str(input("First Name: ")),
                "last_name" : str(input("Last Name: ")),
                "id_number" : int(input("ID_Number: ")),
                "balance" : float(input("Balance: ")),
                "transactions_to_execute" : [],
                "transaction_history" : [],
                })
            except:
                print("\nWrong Key. Please try again\n")
                continue
            bank_accounts [new_account_number] = new_account
            print(f"New Account created successfully!\nAccount Number: {new_account_number}\nAccount Details: {bank_accounts[new_account_number]}")
        elif operation.lower() == "e":
            try:
                account_number: int = int(input(f"Which account number would you like to perform actions for?\n Available accounts are:\n {list(bank_accounts.keys())}"))
            except ValueError as ex:
                print(f"\nError occurred with - {ex}. Please try again:\n")
                continue
            if not account_number in bank_accounts:
                print("\nSorry, this account number is not valid\n")
                continue
            if account_number in bank_accounts:
                action: str = str(input(f"Would you like to:\n Make a New Transaction [Press 1]\n Execute all the Existing Transactions [Press 2]\n"))
                if action == '1':
                    des_account:int = int(input("To which account should you make the transaction?"))
                    if not des_account in bank_accounts:
                        print("\nSorry, this account number does not exist in the system\n")
                        continue
                    else:
                        trans_amount: int = int(input("What's the amount for transaction?"))
                        trans_details: tuple = (datetime.now().strftime("%Y-%m-%d %H:%M:%S"),account_number,des_account,trans_amount)
                        bank_accounts [account_number]["transactions_to_execute"].append(trans_details)
                elif action == '2':
                    try:
                        trans_index: int = int(input(f"Which transaction would you like to execute? choose  0 - {len(bank_accounts [account_number]["transactions_to_execute"])-1}"))
                        trans_to_execute = (bank_accounts[account_number]["transactions_to_execute"][trans_index])
                        trans_to_execute = (list(trans_to_execute))
                        trans_to_execute[0] = (datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                        trans_to_execute = (tuple(trans_to_execute))
                        bank_accounts [account_number]["transaction_history"].append(trans_to_execute)
                        trans_amount = trans_to_execute [3]
                        bank_accounts[account_number].update({"balance": bank_accounts [account_number] ["balance"] - trans_amount})
                        des_account = bank_accounts[account_number]["transactions_to_execute"][trans_index][2]
                        bank_accounts[des_account].update({"balance": bank_accounts[des_account]["balance"] + trans_amount})
                        del (bank_accounts[account_number]["transactions_to_execute"][trans_index])
                    except:
                        print("Out of range. Please try again")
                        continue
                else:
                    print("Sorry, this option is invalid")
                    continue
        elif operation.lower() == "r":
            try:
                report_operation: int = int(input("Would you like to: \nDisplay all Bank Reports [Press 1]\
                 \nLocate an Existing Account [Press 2]\
                  \nLocate Customer by ID [Press 3]\
                   \nLocate Customer by First Name [Press 4]\
                    \nDisplay all Accounts Sorted by Balance [Press 5]\
                     \nDisplay all Transactions Sorted by Time of Transaction [Press 6]\
                      \nDisplay all Transactions from Today [Press 7]\
                       \nDisplay all Transactions with Negative Balance [Press 8]\
                        \nDisplay the Total Balance from all Accounts [Press 9]"))
                match report_operation:
                    case 1: printing_accounts(bank_accounts)
                    case 2: account_by_number()
                    case 3: account_by_id()
                    case 4: account_by_name()
                    case 5: sorted_by_balance()
                    case 6: history_transactions_sorted ()
                    case 7: today_transactions ()
                    case 8: negative_balance ()
                    case 9: all_balances ()
                    case _: print("\nWrong Key\n")
            except ValueError as e:
                print(f"\nAn Unexpected Error occurred with - {e}. Please try again\n")
        elif operation.lower() == "q":
            print("Quitting the program")
            break
        else:
            print("\nWrong Key, Please try again\n")

if __name__== "__main__":
    main_menu()
