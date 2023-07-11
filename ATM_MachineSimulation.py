class InsufficientFundsException(Exception):
    pass


class InvalidDepositAmountException(Exception):
    pass


class InvalidAmountException(Exception):
    pass


class BankAccount:
    def __init__(self):
        self.__accountBalance = 1000

    def depositAmount(self, depositAmnt):
        self.__accountBalance += depositAmnt
        return self.__accountBalance

    def withdrawAmount(self, withdrawAmnt):
        self.__accountBalance -= withdrawAmnt
        return self.__accountBalance


bankAccount = BankAccount()
while True:
    try:
        userCommand = input("\nPress 'D' to Deposit : \nPress 'W' to Withdraw : \nPress 'C' to check balance : \nPress 0 to end the session : ")
        if userCommand == 'D':
            depositAmount = int(input("Enter the amount to be deposited : "))
            if depositAmount <= 0:
                raise InvalidDepositAmountException
            else:
                bankAccount.depositAmount(depositAmount)
                print("Current balance : Rs.", bankAccount._BankAccount__accountBalance)
        elif userCommand == 'W':
            withdrawalAmount = int(input("Enter the amount to be withdrawn : "))
            if withdrawalAmount <= 0:
                raise InvalidAmountException
            if withdrawalAmount > bankAccount._BankAccount__accountBalance:
                print("Current balance : Rs.", bankAccount._BankAccount__accountBalance)
                raise InsufficientFundsException
            else:
                bankAccount.withdrawAmount(withdrawalAmount)
                print("Current balance : Rs.", bankAccount._BankAccount__accountBalance)
                if bankAccount._BankAccount__accountBalance < 1000:
                    print("Current balance is less than minimum balance")
        elif userCommand == 'C':
            print("Your current balance : Rs.", bankAccount._BankAccount__accountBalance)
            if bankAccount._BankAccount__accountBalance < 1000:
                print("Current balance is less than minimum balance")
        elif userCommand == '0':
            print("Session ended.")
            break
        else:
            print("Invalid Input.")
    except InsufficientFundsException:
        print("InsufficientFundsException : The withdrawal amount is higher than the account balance.")
    except InvalidDepositAmountException:
        print("InvalidDepositAmountException : The deposit amount is not valid, the value should be greater than zero.")
    except InvalidAmountException:
        print("InvalidAmountException : The withdrawal amount is should be greater than zero.")
