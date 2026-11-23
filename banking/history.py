"""Transaction record definitions and in-memory history storage."""

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Literal


TransactionType = Literal["deposit", "withdrawal"]


@dataclass(frozen=True)
class Transaction:
    """An immutable record of one successful account transaction."""

    transaction_id: str
    account_number: str
    transaction_type: TransactionType
    amount: Decimal
    timestamp: datetime
    balance_after: Decimal


class TransactionHistory:
    """Store successful transactions separately for each account."""

    def __init__(self) -> None:
        self._transactions: dict[str, list[Transaction]] = {}

    def add(self, transaction: Transaction) -> None:
        """Add a successful transaction to its account's history."""
        self._transactions.setdefault(transaction.account_number, []).append(
            transaction
        )

    def get_for_account(self, account_number: str) -> list[Transaction]:
        """Return a copy of the transaction history for one account."""
        return list(self._transactions.get(account_number, []))
