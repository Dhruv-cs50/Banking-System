import shelve

def save_accounts_to_file(accounts):
    try:
        with shelve.open("accounts_db") as db:
            for name, account in accounts.items():
                db[name] = account
        print("Accounts saved successfully.")
    except Exception as e:
        print(f"Error saving accounts: {e}")

def load_accounts_from_file():
    accounts = {}
    try:
        with shelve.open("accounts_db") as db:
            for name in db:
                accounts[name] = db[name]
        print("Accounts loaded successfully.")
    except Exception as e:
        print(f"Error loading accounts: {e}")
    return accounts