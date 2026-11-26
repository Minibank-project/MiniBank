
import string
import random


class Account:
    def __init__(self, name, pin, account_number):
        self.name = name
        self.pin = pin
        self.account_number = account_number
        self.balance = 0

    def get_details(self):
        return {
            "Name": self.name,
            "AccountNumber": self.account_number,
            "Balance": self.balance
        }


class AccountManager:
    def __init__(self):
        self.accounts = []

    def generate_account_number(self):
        while True:
            digits = "".join(
                random.choices(string.digits, k=7)
            )

            account_number = f"021{digits}"

            # Make sure the account number is unique
            if not any(
                account.account_number == account_number
                for account in self.accounts
            ):
                return account_number

    def create_account(self, name, pin):
        account_number = self.generate_account_number()

        account = Account(name, pin, account_number)

        self.accounts.append(account)

        return account
