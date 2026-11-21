# MiniBank

MiniBank is a small Python command-line banking simulation built to practise professional Git and GitHub collaboration.

> **Educational project only.** MiniBank is not a real banking service and must not be used to store real money, payment credentials, or sensitive financial information.

## Project goals

- Create and manage multiple independent accounts.
- Support deposits and withdrawals with reliable money handling.
- Record successful transactions with timezone-aware timestamps.
- Practise a two-developer workflow using feature branches, pull requests, independent reviews, and automated tests.

## Planned features

- Account creation with an optional account-holder name.
- Unique account numbers and account lookup/listing.
- Deposit and withdrawal operations.
- Per-account transaction history.
- Validation for invalid amounts, unknown accounts, and insufficient funds.

The initial implementation is planned as an in-memory application. Persistence and any additional features require team agreement before implementation.

## Technology

- Python 3
- `Decimal` for monetary values (never binary floating-point `float`).
- Timezone-aware date/time values.
- `pytest` for automated tests.

## Repository structure

```text
MiniBank/
├── banking/
│   ├── __init__.py
│   ├── accounts.py
│   ├── transactions.py
│   └── history.py
├── tests/
├── .github/
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── workflows/
│       └── python-tests.yml
├── docs/
│   ├── PROJECT_BRIEF.md
│   ├── CONTRIBUTING.md
│   └── GIT_WORKFLOW.md
├── main.py
├── requirements-dev.txt
├── README.md
└── .gitignore
```

Some planned application and test files will be added as their tasks are agreed and implemented.

## Getting started

1. Install Python 3.10 or newer.
2. Clone the repository.
3. Create and activate a virtual environment.
4. Install development dependencies:

   ```bash
   python -m pip install -r requirements-dev.txt
   ```

5. Run the test suite:

   ```bash
   python -m pytest
   ```

## Collaboration workflow

- `main` is the stable release branch.
- `develop` is the shared integration branch.
- Create task branches from the latest `develop` branch using `feature/<short-task-name>`, `fix/<short-task-name>`, or another agreed prefix.
- Open pull requests into `develop`.
- The other developer reviews; authors must not approve their own pull requests.
- Automated checks must pass and review conversations must be resolved before merging.
- Release changes from `develop` to `main` through a pull request.

Read [the project brief](docs/PROJECT_BRIEF.md), [contribution guide](docs/CONTRIBUTING.md), and [Git workflow](docs/GIT_WORKFLOW.md) before starting work.
