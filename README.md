# Simple Banking System

A Python-based banking system that allows users to create, manage, and store bank accounts using `shelve` for persistent storage. The system supports **savings** and **checking** accounts, each with specific withdrawal fees.

## Features
- Create a **SavingAccount** (withdrawal fee: $1) or **CheckingAccount** (withdrawal fee: $2).
- Deposit and withdraw money with error handling.
- Check account balances.
- Persistent storage using `shelve`.
- Custom exception handling for invalid transactions.

## Project Structure
```
/SimpleBankingSystem
│── main.py              # Entry point for the application
│── bank_account.py      # Base BankAccount class
│── saving_account.py    # SavingsAccount class
│── checking_account.py  # CheckingAccount class
│── storage.py          # Handles file I/O with shelve
│── exceptions.py       # Custom exception classes
│── accounts_db         # Shelve database file (created on runtime)
```

## Installation & Setup
### Prerequisites
Ensure you have **Python 3.x** installed.

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/SimpleBankingSystem.git
   ```
2. Navigate to the project folder:
   ```bash
   cd SimpleBankingSystem
   ```
3. Run the application:
   ```bash
   python main.py
   ```

## Usage
### Menu Options
1. **Create a new account**: Enter your name and select an account type (saving/checking).
2. **Deposit money**: Choose an account and enter a deposit amount.
3. **Withdraw money**: Choose an account and enter a withdrawal amount (fees apply).
4. **Check balance**: View your account balance.
5. **Save account data**: Store current account data using `shelve`.
6. **Load account data**: Retrieve stored accounts from `shelve`.
7. **Exit**: Close the application.

## Exception Handling
- **NegativeAmountError**: Raised for negative deposits or withdrawals.
- **InsufficientFundsError**: Raised when attempting to withdraw more than available balance.

## Future Enhancements
- Implement **unit tests**.
- Add **transaction history tracking**.
- Improve UI with a web-based dashboard.

## License
This project is open-source under the MIT License.

## Contributing
Feel free to submit **issues** or **pull requests** to improve this project!

