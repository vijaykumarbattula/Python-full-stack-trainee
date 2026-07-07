#USER DATABASE

users = {
    12345: {
        "name": "vijay",
        "Email": "vk7802814@gmail.com",
        "balance": 10000,
        "password": "1234"
    },
    12345: {
        "name": "kumar",
        "Email": "chinnababubathula@gmail.com",
        "balance": 50000,
        "password": "1235"
    }
}

#REGISTER

def register(name: str, email: str, initial_deposit: int, password: str):

    account = max(users.keys()) + 1

    users[account] = {
        "name": name,
        "Email": email,
        "balance": initial_deposit,
        "password": password
    }

    print("\nRegistration Successful")
    print(f"Your Account Number is : {account}")


#LOGIN

def login(account: int, password: str) -> bool:

    if account in users:

        if users[account]["password"] == password:
            print("\nLogin Successful")
            return True

        else:
            print("Incorrect Password")
            return False

    else:
        print("Account Not Found")
        return False


#BALANCE

def balance(account: int) -> int:
    return users[account]["balance"]


# WITHDRAW

def withdraw(account: int, withdraw_amount: int) -> str:

    if withdraw_amount <= users[account]["balance"]:

        users[account]["balance"] -= withdraw_amount

        return f"Withdrawal Successful\nAvailable Balance : {users[account]['balance']}"

    else:
        return "Insufficient Balance"


#DEPOSIT

def deposit(account: int, deposit_amount: int):

    users[account]["balance"] += deposit_amount

    print("Deposit Successful")
    print(f"Available Balance : {users[account]['balance']}")


# TRANSFER 

def transfer(sender: int, receiver: int, transfer_amount: int):

    if receiver not in users:
        print("Receiver Account Not Found")
        return

    if transfer_amount <= users[sender]["balance"]:

        users[sender]["balance"] -= transfer_amount
        users[receiver]["balance"] += transfer_amount

        print("Transfer Successful")
        print(f"Available Balance : {users[sender]['balance']}")

    else:
        print("Insufficient Balance")


# MINI STATEMENT

def ministatement(account: int):

    print("\n========== MINI STATEMENT ==========")
    print(f"Account Number : {account}")
    print(f"Name           : {users[account]['name']}")
    print(f"Email          : {users[account]['Email']}")
    print(f"Balance        : {users[account]['balance']}")
    print("====================================")


# LOGOUT 

def logout():

    print("Logout Successful")
    return False


#                        MAIN PROGRAM 

if __name__ == "__main__":

    while True:

        print("\n========== SMALL SCALE BANK ==========")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = int(input("Enter Your Choice : "))

        # Register
        if choice == 1:

            name = input("Enter Name : ")
            email = input("Enter Email : ")
            deposit_amount = int(input("Enter Initial Deposit : "))
            password = input("Create Password : ")

            register(name, email, deposit_amount, password)

        # Login
        elif choice == 2:

            account = int(input("Enter Account Number : "))
            password = input("Enter Password : ")

            login_val = login(account, password)

            while login_val:

                print("\n========== BANK SERVICES ==========")
                print("1. Balance")
                print("2. Withdraw")
                print("3. Deposit")
                print("4. Transfer")
                print("5. Mini Statement")
                print("6. Logout")

                service = int(input("Enter Your Choice : "))

                if service == 1:

                    current_balance = balance(account)

                    print(f"Current Balance : {current_balance}")

                elif service == 2:

                    amount = int(input("Enter Withdraw Amount : "))

                    result = withdraw(account, amount)

                    print(result)

                elif service == 3:

                    amount = int(input("Enter Deposit Amount : "))

                    deposit(account, amount)

                elif service == 4:

                    receiver = int(input("Enter Receiver Account Number : "))
                    amount = int(input("Enter Transfer Amount : "))

                    transfer(account, receiver, amount)

                elif service == 5:

                    ministatement(account)

                elif service == 6:

                    login_val = logout()

                else:

                    print("Invalid Choice")

        # Exit
        elif choice == 3:

            print("Thank You for Visiting Small Scale Bank")
            break

        else:

            print("Invalid Choice")