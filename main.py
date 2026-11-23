from banking.accounts import Account


"""MiniBank command-line entry point.

The application flow will be implemented after the account and transaction
interfaces have been agreed by the team.
"""


def main():
    """Run MiniBank once the application flow is implemented."""
    user = Account()

    print(user.accounts)



if __name__ == "__main__":
    main()
