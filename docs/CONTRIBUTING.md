# Contributing to MiniBank

Thanks for contributing. MiniBank is a two-developer learning project, and the quality of the collaboration process matters as much as the application.

## Before starting

1. Read the README and project brief.
2. Read the Git workflow guide.
3. Check the GitHub issues or the task agreed by the team.
4. Confirm the module interface with the other developer before building dependent functionality.

Do not independently introduce features or expand the agreed scope.

## Development environment

Use Python 3.10 or newer. Create a virtual environment and install development dependencies:

```bash
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows PowerShell
.venv\Scripts\Activate.ps1

python -m pip install -r requirements-dev.txt
```

Run tests with:

```bash
python -m pytest
```

## Coding standards

- Prefer clear, readable Python over clever or unnecessarily abstract code.
- Use descriptive names and small functions with focused responsibilities.
- Add type hints to public functions where practical.
- Keep account management, transaction operations, and transaction history responsibilities separated.
- Use `Decimal` for all monetary calculations. Do not convert money to `float`.
- Use timezone-aware timestamps.
- Validate inputs before changing balances or writing successful transaction records.
- Avoid unrelated refactors in task branches.
- Do not commit secrets, credentials, personal financial information, virtual environments, or generated cache files.

## Tests

Every behavior change should include or update tests. Include relevant edge cases, especially:

- Zero and negative amounts.
- Invalid amount formats.
- Unknown account numbers.
- Withdrawals exceeding the available balance.
- Account isolation.
- Failed operations leaving balances and history unchanged.

Tests should be deterministic and must not depend on real banking services or network calls.

## Commit messages

Use a short, descriptive conventional-style prefix:

- `feat:` new functionality
- `fix:` bug fixes
- `test:` tests
- `docs:` documentation
- `refactor:` code restructuring without behavior change
- `chore:` maintenance and tooling

Examples:

```text
feat: add account creation
feat: implement deposit operation
fix: prevent withdrawal beyond balance
test: cover invalid transaction amounts
docs: explain pull request workflow
```

## Pull requests

- Open pull requests into `develop`, not directly into `main`.
- Use the repository pull request template.
- Explain what changed and how it was tested.
- Request review from the other developer.
- Do not approve your own pull request.
- Respond to review comments and resolve conversations only after the concern has been addressed.
- Keep the pull request focused on one task.
- Do not merge while required checks are failing or review conversations remain unresolved.

## Review expectations

Reviewers should check correctness, edge cases, readability, tests, scope, and module boundaries. Comments should explain the concern and, where useful, suggest a concrete improvement.

A review is not a competition. Ask questions when intent is unclear and discuss interface changes before merging.

## Scope changes

New features, persistence, and changes to agreed public interfaces require discussion and agreement from both developers before implementation.
