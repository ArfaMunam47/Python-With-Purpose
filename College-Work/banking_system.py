
# 11-10-2026
# PYTHON ASSIGNMENT

"""
============================================================
                 BANKING MANAGEMENT SYSTEM
============================================================
Project type : Terminal / Console Based
Language     : Python
Storage      : Local JSON file (created automatically)

Run this file with:
    python banking_system.py

This is an educational project, not a real banking application.
Passwords are hashed before they are saved.
Password characters are visible while typing so input works
reliably in PyCharm's Run window.
============================================================
"""

import json
import os
import random
import hashlib
import hmac
from datetime import datetime


# ============================================================
# 1. PROJECT SETTINGS
# ============================================================

DATA_FILE = "banking_data.json"
STARTING_CREDIT_SCORE = 650
MIN_PASSWORD_LENGTH = 6


# ============================================================
# 2. FILE HANDLING
# ============================================================

def load_accounts():
    """Load saved accounts from the JSON file."""
    if not os.path.exists(DATA_FILE):
        return {}

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, dict):
            return data

        print("Warning: The data file has an invalid format.")
        return {}

    except (json.JSONDecodeError, OSError):
        print("Warning: Could not read the saved data file.")
        return {}


def save_accounts(accounts):
    """Save all accounts in the local JSON file."""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(accounts, file, indent=4)
    except OSError:
        print("Error: Account information could not be saved.")


# ============================================================
# 3. COMMON / HELPER FUNCTIONS
# ============================================================

def print_heading(title):
    """Print a neat heading in the console."""
    print("\n" + "=" * 60)
    print(title.center(60))
    print("=" * 60)


def get_password(prompt):
    """
    Use input() instead of getpass().
    This avoids the blank-input problem in PyCharm's Run console.
    Password characters will be visible while typing.
    """
    return input(prompt).strip()


def create_password_hash(password):
    """Create a salted password hash instead of storing plain text."""
    salt = os.urandom(16)
    password_hash = hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), salt, 100000
    )
    return salt.hex(), password_hash.hex()


def check_password(entered_password, saved_salt, saved_hash):
    """Check the entered password against the saved hash."""
    salt = bytes.fromhex(saved_salt)
    entered_hash = hashlib.pbkdf2_hmac(
        "sha256", entered_password.encode("utf-8"), salt, 100000
    ).hex()
    return hmac.compare_digest(entered_hash, saved_hash)


def generate_account_number(accounts):
    """Generate a unique 10-digit account number."""
    while True:
        number = str(random.randint(1000000000, 9999999999))
        if number not in accounts:
            return number


def find_account_by_name(accounts, name):
    """Find an account using the account holder's name."""
    for account_number, account in accounts.items():
        if account["name"].casefold() == name.casefold():
            return account_number
    return None


def get_positive_amount(prompt):
    """Get a valid amount greater than zero."""
    try:
        amount = float(input(prompt).strip())

        if amount <= 0:
            print("Amount must be greater than zero.")
            return None

        return round(amount, 2)

    except ValueError:
        print("Please enter a valid number, for example 5000.")
        return None


def add_transaction(account, transaction_type, amount, description):
    """Add a transaction record to the user's statement."""
    account["transactions"].append({
        "date": datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"),
        "type": transaction_type,
        "amount": round(amount, 2),
        "balance": round(account["balance"], 2),
        "description": description
    })


# ============================================================
# 4. CREATE NEW BANK ACCOUNT
# ============================================================

def create_account(accounts):
    """Create a new account after validating name and CNIC."""
    print_heading("CREATE NEW BANK ACCOUNT")

    # Validate full name.
    while True:
        name = input("Enter your full name: ").strip()

        if len(name) < 3 or not any(char.isalpha() for char in name):
            print("Please enter a valid full name.")
            continue

        if find_account_by_name(accounts, name) is not None:
            print("This name is already registered in this demo.")
            print("Please use a different name.")
            return

        break

    # Validate CNIC: exactly 13 digits, without dashes.
    while True:
        cnic = input("Enter your 13-digit CNIC (without dashes): ").strip()

        if len(cnic) != 13 or not cnic.isdigit():
            print("Invalid CNIC. It must contain exactly 13 digits.")
            continue

        already_registered = any(
            account["cnic"] == cnic for account in accounts.values()
        )

        if already_registered:
            print("This CNIC is already registered.")
            return

        break

    # Create and confirm password.
    while True:
        password = get_password(
            "Create a password (minimum 6 characters): "
        )

        if len(password) < MIN_PASSWORD_LENGTH:
            print("Password must contain at least 6 characters.")
            continue

        confirm = get_password("Confirm your password: ")

        if password != confirm:
            print("Passwords do not match. Try again.")
            continue

        break

    # Generate account number and password hash.
    account_number = generate_account_number(accounts)
    salt, password_hash = create_password_hash(password)

    # Store account details.
    accounts[account_number] = {
        "name": name,
        "cnic": cnic,
        "salt": salt,
        "password_hash": password_hash,
        "balance": 0.0,
        "credit_score": STARTING_CREDIT_SCORE,
        "transactions": []
    }

    add_transaction(
        accounts[account_number],
        "ACCOUNT CREATED",
        0,
        "New bank account opened"
    )

    save_accounts(accounts)

    print_heading("ACCOUNT CREATED SUCCESSFULLY")
    print("Account Holder :", name)
    print("Account Number :", account_number)
    print("Opening Balance: Rs. 0.00")
    print("Credit Score   :", STARTING_CREDIT_SCORE)
    print("-" * 60)
    print("Please remember your account number and password.")


# ============================================================
# 5. USER LOGIN / AUTHENTICATION
# ============================================================

def user_login(accounts):
    """Check the user's name and password before allowing access."""
    print_heading("USER LOGIN")

    name = input("Enter your full name: ").strip()
    account_number = find_account_by_name(accounts, name)

    if account_number is None:
        print("Account not found. Please check your name.")
        return None

    password = get_password("Enter your account password: ")
    account = accounts[account_number]

    if check_password(password, account["salt"], account["password_hash"]):
        print("\nLogin successful. Welcome,", account["name"] + "!")
        return account_number

    print("Incorrect password. Login failed.")
    return None


# ============================================================
# 6. CHECK BALANCE
# ============================================================

def check_balance(account):
    """Display the current account balance."""
    print_heading("ACCOUNT BALANCE")
    print("Account Holder  :", account["name"])
    print("Current Balance : Rs.", format(account["balance"], ",.2f"))


# ============================================================
# 7. DEPOSIT MONEY
# ============================================================

def deposit_money(account, accounts):
    """Deposit money and update the transaction history."""
    print_heading("DEPOSIT MONEY")
    amount = get_positive_amount("Enter deposit amount (Rs.): ")

    if amount is None:
        return

    account["balance"] = round(account["balance"] + amount, 2)

    # This educational project increases the score by 2 per deposit.
    account["credit_score"] = min(850, account["credit_score"] + 2)

    add_transaction(account, "DEPOSIT", amount, "Money deposited")
    save_accounts(accounts)

    print("Deposit successful!")
    print("Deposited Amount: Rs.", format(amount, ",.2f"))
    print("New Balance     : Rs.", format(account["balance"], ",.2f"))


# ============================================================
# 8. WITHDRAW MONEY
# ============================================================

def withdraw_money(account, accounts):
    """Withdraw money only if sufficient balance is available."""
    print_heading("WITHDRAW MONEY")
    amount = get_positive_amount("Enter withdrawal amount (Rs.): ")

    if amount is None:
        return

    if amount > account["balance"]:
        print("Transaction declined: insufficient balance.")
        print("Available Balance: Rs.", format(account["balance"], ",.2f"))
        return

    account["balance"] = round(account["balance"] - amount, 2)

    add_transaction(account, "WITHDRAWAL", amount, "Money withdrawn")
    save_accounts(accounts)

    print("Withdrawal successful!")
    print("Withdrawn Amount : Rs.", format(amount, ",.2f"))
    print("Remaining Balance: Rs.", format(account["balance"], ",.2f"))


# ============================================================
# 9. BANK STATEMENT
# ============================================================

def bank_statement(account):
    """Display the complete transaction history."""
    print_heading("BANK STATEMENT")
    print("Account Holder :", account["name"])
    print("Current Balance: Rs.", format(account["balance"], ",.2f"))
    print("-" * 60)

    if not account["transactions"]:
        print("No transactions are available.")
        return

    for number, transaction in enumerate(account["transactions"], start=1):
        print("\nTransaction Number:", number)
        print("Date        :", transaction["date"])
        print("Type        :", transaction["type"])
        print("Amount      : Rs.", format(transaction["amount"], ",.2f"))
        print("Description :", transaction["description"])
        print("Balance     : Rs.", format(transaction["balance"], ",.2f"))
        print("-" * 60)

    print("End of statement.")


# ============================================================
# 10. CREDIT SCORE AND LOAN ELIGIBILITY
# ============================================================

def credit_score_and_loan(account):
    """Show the user's credit score and educational loan limit."""
    print_heading("CREDIT SCORE AND LOAN ELIGIBILITY")

    score = account["credit_score"]

    if score >= 800:
        category = "Excellent"
        loan_limit = 500000
    elif score >= 750:
        category = "Very Good"
        loan_limit = 300000
    elif score >= 700:
        category = "Good"
        loan_limit = 200000
    elif score >= 650:
        category = "Fair"
        loan_limit = 100000
    else:
        category = "Low"
        loan_limit = 0

    print("Account Holder :", account["name"])
    print("Credit Score   :", score, "/ 850")
    print("Credit Category:", category)
    print("Loan Eligibility: Rs.", format(loan_limit, ",.2f"))

    if loan_limit == 0:
        print("You are not eligible for a loan in this demo.")
    else:
        print("You may qualify for a loan up to the amount shown.")

    print("\nNote: This is a simplified student-project calculation,")
    print("not a real bank credit assessment or loan approval.")


# ============================================================
# 11. USER DASHBOARD
# ============================================================

def user_dashboard(account_number, accounts):
    """Display banking options after successful login."""
    account = accounts[account_number]

    while True:
        print_heading("USER BANKING DASHBOARD")
        print("Welcome,", account["name"])
        print("Account Number:", account_number)
        print("-" * 60)
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Bank Statement")
        print("5. Credit Score and Loan Eligibility")
        print("6. Logout")
        print("-" * 60)

        choice = input("Select an option (1-6): ").strip()

        if choice == "1":
            check_balance(account)
        elif choice == "2":
            deposit_money(account, accounts)
        elif choice == "3":
            withdraw_money(account, accounts)
        elif choice == "4":
            bank_statement(account)
        elif choice == "5":
            credit_score_and_loan(account)
        elif choice == "6":
            print("You have been logged out successfully.")
            break
        else:
            print("Invalid option. Select a number from 1 to 6.")

        input("\nPress Enter to return to the dashboard...")


# ============================================================
# 12. MAIN MENU
# ============================================================

def main():
    """Start the Banking Management System."""
    accounts = load_accounts()

    while True:
        print_heading("WELCOME TO PYTHON BANK")
        print("1. Create New Account")
        print("2. Login to Existing Account")
        print("3. Exit")
        print("-" * 60)

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            create_account(accounts)
            input("\nPress Enter to return to the main menu...")

        elif choice == "2":
            if not accounts:
                print("No accounts found. Please create an account first.")
                input("\nPress Enter to continue...")
                continue

            account_number = user_login(accounts)

            if account_number is not None:
                input("\nPress Enter to open your dashboard...")
                user_dashboard(account_number, accounts)
            else:
                input("\nPress Enter to return to the main menu...")

        elif choice == "3":
            print_heading("THANK YOU FOR USING PYTHON BANK")
            print("Your banking session has ended.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            input("\nPress Enter to try again...")


# ============================================================
# 13. PROGRAM STARTING POINT
# ============================================================

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram stopped. Thank you for using Python Bank.")

