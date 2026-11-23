"""Deposit and withdrawal operations for MiniBank accounts."""

from datetime import datetime
from decimal import Decimal
from typing import Protocol
from uuid import uuid4

from banking.history import Transaction, TransactionHistory, TransactionType


class AccountLike(Protocol):
    """The minimal account interface required by transaction operations.

    The account-management module owns the actual Account implementation and
    remains the source of truth for the account number and balance.
    """

    account_number: str
    balance: Decimal


class TransactionService:
    """Validate and process transactions against existing account objects."""

    def __init__(self, history: TransactionHistory | None = None) -> None:
        self._history = history if history is not None else TransactionHistory()

    def deposit(self, account: AccountLike, amount: Decimal) -> Transaction:
        """Deposit a positive Decimal amount into an existing account."""
        return self._execute(account, amount, "deposit")

    def withdraw(self, account: AccountLike, amount: Decimal) -> Transaction:
        """Withdraw a positive Decimal amount from an existing account."""
        return self._execute(account, amount, "withdrawal")

    def get_history(self, account_number: str) -> list[Transaction]:
        """Retrieve successful transactions for the supplied account number."""
        return self._history.get_for_account(account_number)

    def _execute(
        self,
        account: AccountLike,
        amount: Decimal,
        transaction_type: TransactionType,
    ) -> Transaction:
        self._validate_amount(amount)
        self._validate_balance(account.balance)

        if transaction_type == "withdrawal" and amount > account.balance:
            raise ValueError("Insufficient funds.")

        new_balance = (
            account.balance + amount
            if transaction_type == "deposit"
            else account.balance - amount
        )

        transaction = Transaction(
            transaction_id=str(uuid4()),
            account_number=account.account_number,
            transaction_type=transaction_type,
            amount=amount,
            timestamp=datetime.now().astimezone(),
            balance_after=new_balance,
        )

        # Validation is complete before the account or history is changed.
        account.balance = new_balance
        self._history.add(transaction)
        return transaction

    @staticmethod
    def _validate_amount(amount: Decimal) -> None:
        if not isinstance(amount, Decimal):
            raise TypeError("Transaction amount must be a Decimal.")
        if not amount.is_finite() or amount <= Decimal("0"):
            raise ValueError("Transaction amount must be a finite value greater than zero.")

    @staticmethod
    def _validate_balance(balance: Decimal) -> None:
        if not isinstance(balance, Decimal) or not balance.is_finite():
            raise ValueError("Account balance must be a finite Decimal value.")
