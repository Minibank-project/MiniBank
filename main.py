from banking.accounts import AccountManager


def main():
  bank = AccountManager()
  
  name = input("Enter your full name: ")
  pin = input("Create your PIN: ")
  
  account = bank.create_account(name, pin)
  
  print("\nAccount created successfully!")
  print(f"Name: {account.name}")
  print(f"Account number: {account.account_number}")
  print(f"Balance: ₦{account.balance}")


if __name__ == "__main__":
  main()