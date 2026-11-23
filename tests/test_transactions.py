"""Tests for deposits, withdrawals, and transaction history."""

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal

import pytest

from banking.history import TransactionHistory
from banking.transactions import TransactionService


@dataclass
class FakeAccount:
    """Test double matching the agreed Account interface from Part A."""

    account_number: str
    balance: Decimal = Decimal("0.00")


@pytest.fixture
def service() -> TransactionService:
    return TransactionService(TransactionHistory())


def test_deposit_updates_balance_and_records_transaction(
    service: TransactionService,
) -> None:
    account = FakeAccount("MB1001", Decimal("100.00"))

    transaction = service.deposit(account, Decimal("50.25"))

    assert account.balance == Decimal("150.25")
    assert transaction.account_number == "MB1001"
    assert transaction.transaction_type == "deposit"
    assert transaction.amount == Decimal("50.25")
    assert transaction.balance_after == Decimal("150.25")
    assert transaction in service.get_history("MB1001")


def test_withdrawal_updates_balance_and_records_transaction(
    service: TransactionService,
) -> None:
    account = FakeAccount("MB1002", Decimal("100.00"))

    transaction = service.withdraw(account, Decimal("35.50"))

    assert account.balance == Decimal("64.50")
    assert transaction.transaction_type == "withdrawal"
    assert transaction.balance_after == Decimal("64.50")
    assert transaction in service.get_history("MB1002")


def test_transaction_timestamp_is_timezone_aware(
    service: TransactionService,
) -> None:
    transaction = service.deposit(
        FakeAccount("MB1003"),
        Decimal("10.00"),
    )

    assert isinstance(transaction.timestamp, datetime)
    assert transaction.timestamp.tzinfo is not None
    assert transaction.timestamp.utcoffset() is not None


@pytest.mark.parametrize(
    "amount",
    [
        Decimal("0"),
        Decimal("-1"),
        Decimal("NaN"),
        Decimal("Infinity"),
    ],
)
def test_invalid_decimal_amount_does_not_change_balance_or_history(
    service: TransactionService,
    amount: Decimal,
) -> None:
    account = FakeAccount("MB1004", Decimal("75.00"))

    with pytest.raises(ValueError):
        service.deposit(account, amount)

    assert account.balance == Decimal("75.00")
    assert service.get_history("MB1004") == []


@pytest.mark.parametrize("amount", [10.0, 10, "10.00"])
def test_non_decimal_amount_is_rejected(
    service: TransactionService,
    amount: object,
) -> None:
    account = FakeAccount("MB1005", Decimal("75.00"))

    with pytest.raises(TypeError):
        service.deposit(account, amount)  # type: ignore[arg-type]

    assert account.balance == Decimal("75.00")
    assert service.get_history("MB1005") == []


def test_withdrawal_over_balance_is_rejected_without_side_effects(
    service: TransactionService,
) -> None:
    account = FakeAccount("MB1006", Decimal("20.00"))

    with pytest.raises(ValueError, match="Insufficient funds"):
        service.withdraw(account, Decimal("20.01"))

    assert account.balance == Decimal("20.00")
    assert service.get_history("MB1006") == []


def test_history_is_separated_by_account(
    service: TransactionService,
) -> None:
    first_account = FakeAccount("MB1007", Decimal("10.00"))
    second_account = FakeAccount("MB1008", Decimal("20.00"))

    first_transaction = service.deposit(first_account, Decimal("5.00"))
    second_transaction = service.withdraw(second_account, Decimal("2.00"))

    assert service.get_history("MB1007") == [first_transaction]
    assert service.get_history("MB1008") == [second_transaction]


def test_history_returns_a_copy(
    service: TransactionService,
) -> None:
    account = FakeAccount("MB1009")
    service.deposit(account, Decimal("5.00"))

    records = service.get_history("MB1009")
    records.clear()

    assert len(service.get_history("MB1009")) == 1


def test_each_transaction_has_a_unique_identifier(
    service: TransactionService,
) -> None:
    account = FakeAccount("MB1010")

    first = service.deposit(account, Decimal("1.00"))
    second = service.deposit(account, Decimal("1.00"))

    assert first.transaction_id != second.transaction_id
