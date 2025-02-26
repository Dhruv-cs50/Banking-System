from saving_account import SavingAccount
from checking_account import CheckingAccount
from storage import save_accounts_to_file, load_accounts_from_file
from exceptions import NegativeAmountError, InsufficientFundsError

def main():
    accounts = load_accounts_from_file()

    while True:
        print("\nOptions:")
        print("1. Create a new account")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Check balance")
        print("5. Save account data")
        print("6. Load account data")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter your name: ")
            acc_type = input("Enter account type (saving/checking): ").lower()
            if name in accounts:
                print("Account with this name already exists.")
                continue
            if acc_type == 'saving':
                accounts[name] = SavingAccount(name)
            elif acc_type == 'checking':
                accounts[name] = CheckingAccount(name)
            else:
                print("Invalid account type.")
                continue
            print("Account created successfully. Initial balance: $0")

        elif choice == '2':
            name = input("Enter account name: ")
            if name in accounts:
                try:
                    amount = float(input("Enter deposit amount: "))
                    accounts[name].deposit(amount)
                except (ValueError, NegativeAmountError) as e:
                    print(e)
            else:
                print("Account not found.")

        elif choice == '3':
            name = input("Enter account name: ")
            if name in accounts:
                try:
                    amount = float(input("Enter withdrawal amount: "))
                    accounts[name].withdraw(amount)
                except (ValueError, NegativeAmountError, InsufficientFundsError) as e:
                    print(e)
            else:
                print("Account not found.")

        elif choice == '4':
            name = input("Enter account name: ")
            if name in accounts:
                accounts[name].check_balance()
            else:
                print("Account not found.")

        elif choice == '5':
            save_accounts_to_file(accounts)

        elif choice == '6':
            accounts = load_accounts_from_file()

        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
# Output:2