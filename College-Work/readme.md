# 🏦 Banking Management System

### Python Programming Project

---

## 📌 Assignment Details

| Field | Information |
|---|---|
| **Project Title** | Banking Management System |
| **Student Roll Number** | 47 |
| **Programming Language** | Python |
| **Project Type** | Terminal / Console-Based Application |
| **Project Category** | Banking & Financial Management |
| **Data Storage** | JSON File |
| **User Interface** | Console-Based Interface |
| **Admin Panel** | Not Included (User-Side Only) |

---

## 📖 Project Overview

The **Banking Management System** is a Python-based console application developed as an academic programming assignment.

The main purpose of this project is to simulate basic banking operations through a simple, interactive, and user-friendly terminal interface.

Users can create their own bank accounts, securely log in, check their account balance, deposit and withdraw money, view their complete transaction history, and check their credit score and loan eligibility.

The application stores account information and transaction records in a local JSON file, allowing data to remain available even after the program is closed.

This project demonstrates the practical implementation of Python programming concepts, including functions, conditional statements, loops, file handling, data validation, and exception handling.

---

## ✨ Key Features

### 1. Account Creation
- Register a new bank account.
- Enter full name and 13-digit CNIC.
- Validate CNIC information.
- Automatically generate a unique 10-digit account number.
- Create and confirm an account password.

### 2. User Authentication
- Login using registered full name and password.
- Verify user credentials before accessing banking services.
- Store passwords as salted hashes instead of plain text.

### 3. Balance Inquiry
- View the current account balance.
- Display account holder information.

### 4. Money Deposit
- Deposit money into an existing account.
- Validate the entered amount.
- Automatically update the account balance.
- Record the deposit in transaction history.

### 5. Money Withdrawal
- Withdraw money from the account.
- Check available balance before processing withdrawals.
- Prevent withdrawals exceeding the available balance.
- Automatically update the remaining balance.

### 6. Bank Statement
- View complete transaction history.
- Display transaction dates and types.
- Show deposited and withdrawn amounts.
- Display account balance after each transaction.

### 7. Credit Score & Loan Eligibility
- Every new account starts with a credit score of 650.
- Credit score increases with successful deposits.
- Display credit score categories.
- Calculate estimated loan eligibility based on the credit score.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| JSON | Local data storage |
| Random Module | Unique account number generation |
| Hashlib | Password hashing |
| HMAC | Secure password comparison |
| Datetime | Transaction date and time |
| OS | File handling |

**Note:** No external Python libraries are required. All modules used in this project are included in Python's standard library.

---

## 📂 Project Structure

```text
Banking_Management_System/
│
├── banking_system.py
│
├── banking_data.json
│
└── README.md
```

**File Description:**

- `banking_system.py` – Main Python file containing the complete banking application.
- `banking_data.json` – Automatically generated file used to store account information and transaction records.
- `README.md` – Project documentation and usage instructions.

---

## ⚙️ Installation & Setup

### Requirements
- Python 3.x
- PyCharm or any Python-supported code editor.
- Windows, Linux, or macOS.

### Step 1: Install Python

Download Python from the official website:

https://www.python.org/downloads/

### Step 2: Download or Clone the Project

Download the project files and open the project folder in your preferred Python IDE.

### Step 3: Run the Application

Open the terminal inside the project directory and execute:

```bash
python banking_system.py
```

The application will start automatically and display the main menu.

**No additional packages or installations are required.**

---

## 🖥️ How to Use the Application

When the program starts, the following menu appears:

```text
============================================================
                  WELCOME TO PYTHON BANK
============================================================

1. Create New Account
2. Login to Existing Account
3. Exit

Enter your choice (1-3):
```

### Account Creation
1. Select option 1.
2. Enter your full name.
3. Enter your 13-digit CNIC without dashes.
4. Create a password.
5. Confirm your password.
6. The system generates a unique account number.

### User Login
1. Select option 2.
2. Enter your registered full name.
3. Enter your account password.
4. After successful authentication, access the banking dashboard.

### Banking Dashboard

The dashboard provides the following services:

```text
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Bank Statement
5. Credit Score and Loan Eligibility
6. Logout
```

Select the desired option to perform the banking operation.

---

## 🔐 Data Storage & Security

- Account information is stored locally in a JSON file.
- Passwords are stored using salted PBKDF2-HMAC-SHA256 hashes.
- CNIC numbers are validated to ensure exactly 13 digits.
- Duplicate CNIC registrations are prevented.
- Account numbers are generated uniquely.
- Transaction history is saved automatically.

---

## 🎯 Learning Objectives

This project demonstrates practical knowledge of:

- Python functions and modular programming.
- Variables and data types.
- Conditional statements.
- Loops and iteration.
- Lists and dictionaries.
- File handling using JSON.
- Password hashing.
- Input validation.
- Exception handling.
- Basic banking logic and calculations.

---

## ⚠️ Important Note

This application is developed strictly for educational and academic purposes.

The credit score and loan eligibility calculations are simplified demonstrations and do not represent actual banking policies or financial assessments.

This project is a local console-based simulation and is not intended for handling real banking transactions or sensitive financial information.

---

## 👨‍🎓 Student Information

**Student Roll Number: 47**

**Project Name:** Banking Management System

**Language:** Python

**Submission Type:** Python Source Code (.py)

---

## 🏁 Conclusion

The Banking Management System provides a practical demonstration of fundamental banking operations using Python.

It combines account management, authentication, financial transactions, transaction history, and credit score calculations into one organized console-based application.

The project helped demonstrate the use of core Python programming concepts in developing a functional, structured, and user-friendly application.

---

**Developed as an academic Python programming assignment.**