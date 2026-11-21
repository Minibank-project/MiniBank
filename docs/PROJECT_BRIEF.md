# MiniBank — Project Brief

**Version:** 1.0  
**Status:** Planning and repository setup

## 1. Purpose

MiniBank is a small Python command-line banking simulation. Its primary learning objective is to practise a professional, review-driven GitHub collaboration workflow with two developers.

It is an educational simulation only. It will not connect to banks, payment processors, or real financial accounts.

## 2. Users and usage

The initial application is a local command-line program. Users can create multiple simulated accounts, deposit and withdraw simulated funds, and inspect transaction history.

## 3. Functional requirements

### Account management

- Create an account.
- Allow an optional account-holder name.
- Assign each account a unique account number.
- Initialize each account with a zero balance.
- Retrieve an account by account number.
- List existing accounts.
- Keep account data isolated so one account's operations do not affect another.

### Transactions

- Deposit money into an existing account.
- Withdraw money from an existing account.
- Record successful transactions with a unique transaction identifier, account number, transaction type, amount, timestamp, and resulting balance.
- Retrieve transaction history for an account.
- Use timezone-aware timestamps, for example `datetime.now().astimezone()`.

### Validation and consistency

- Represent money with Python `Decimal`, not `float`.
- Reject zero and negative transaction amounts.
- Reject malformed amounts and unknown account numbers.
- Reject withdrawals greater than the available balance.
- A failed transaction must not change the account balance or create a successful transaction-history entry.
- Validate inputs before mutating account state.

## 4. Initial technical direction

- Language: Python 3.10 or newer.
- Interface: command line.
- Storage: in-memory for the first version.
- Tests: pytest.
- Monetary values: `Decimal`.
- Timestamps: timezone-aware local timestamps.

The team must agree on the account and transaction data structures and the public module interfaces before implementation. The account module is the source of truth for account identity and balance. Transaction code must not maintain a competing balance.

Suggested module responsibilities:

- `banking/accounts.py`: account creation, identity, balance initialization, lookup, and listing.
- `banking/transactions.py`: deposit and withdrawal operations and transaction validation.
- `banking/history.py`: transaction record representation and per-account history retrieval.

Suggested public operations (names may be adjusted by agreement):

- `create_account(holder_name=None)`
- `get_account(account_number)`
- `list_accounts()`
- `deposit(account, amount)`
- `withdraw(account, amount)`
- `get_history(account_number)`

## 5. Out of scope for version 1

The following are not part of the initial release:

- Real bank or payment-gateway integration.
- User authentication or authorization.
- Web or mobile interfaces and APIs.
- Transfers between accounts.
- Loans, interest, fees, or overdrafts.
- Foreign exchange.
- Persistent database storage or cloud deployment.

JSON/local persistence may be considered later, but only after the team agrees on the requirement and design.

## 6. Team responsibilities

### Developer A — Account Management

- Account creation and unique account numbers.
- Optional account-holder names.
- Initial balance handling.
- Account lookup and listing.
- Tests for account behavior.

### Developer B — Transaction Management

- Deposit and withdrawal operations.
- Transaction validation.
- Transaction records and timestamps.
- Transaction-history retrieval.
- Tests for transaction behavior.

### Shared responsibilities

Both developers participate in interface decisions, integration, cross-module tests, code reviews, conflict resolution, documentation, and the final demonstration.

## 7. Acceptance criteria

The first integrated version is acceptable when:

- Multiple accounts can be created and remain isolated.
- Each account has a unique account number and starts at zero.
- Valid deposits and withdrawals update the correct balance.
- Invalid amounts, unknown accounts, and insufficient funds are handled safely.
- Failed operations leave balances and successful history unchanged.
- Successful transactions have timezone-aware timestamps and correct resulting balances.
- Automated tests cover normal behavior and important edge cases.
- Changes have been reviewed and merged through the agreed GitHub workflow.
