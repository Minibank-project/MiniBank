# MiniBank Git and GitHub Workflow

This guide defines the team's two-developer collaboration process.

## Branch model

- `main`: stable release branch.
- `develop`: shared integration branch.
- `feature/<task-name>`: new functionality.
- `fix/<task-name>`: bug fixes.
- `docs/<task-name>`: documentation-only work.
- `test/<task-name>`: test-only work when useful.

All task branches start from the latest `develop`. Pull requests target `develop`. Releases are proposed from `develop` into `main`.

## 1. Clone the repository

Each developer clones the repository once:

```bash
git clone https://github.com/Minibank-project/MiniBank.git
cd MiniBank
```

## 2. Start from the latest develop

```bash
git switch develop
git pull origin develop
```

## 3. Create a task branch

Use a short name that describes the task:

```bash
git switch -c feature/account-management
```

Examples:

```bash
git switch -c feature/deposit-operation
git switch -c fix/negative-withdrawal
git switch -c docs/contribution-guide
```

## 4. Work and test

Make focused changes. Run the tests before committing:

```bash
python -m pytest
git status
git diff
```

Stage only files relevant to the task:

```bash
git add banking/accounts.py tests/test_accounts.py
git commit -m "feat: add account creation"
```

## 5. Push and open a pull request

```bash
git push -u origin feature/account-management
```

On GitHub, open a pull request with:

- **Base:** `develop`
- **Compare:** your task branch

Complete the pull request template and request the other developer as reviewer.

## 6. Review and update

The reviewer checks the code and leaves actionable comments. The author makes requested changes on the same branch, commits, and pushes again. The pull request updates automatically.

Before merge:

- Required automated checks pass.
- At least one independent approval is present.
- The author has not approved their own pull request.
- All review conversations are resolved.
- The branch is up to date with the target branch if repository rules require it.

## 7. Merge and clean up

Use the repository's agreed merge method (squash merge is the suggested default for this small project). After merge, delete the remote task branch through GitHub.

Update the local integration branch:

```bash
git switch develop
git pull origin develop
git branch -d feature/account-management
```

## 8. Keep a long-running branch current

If `develop` has moved forward while you are working, update your task branch using the team's agreed method. For this project, rebasing a task branch is acceptable if the author is comfortable resolving conflicts:

```bash
git fetch origin
git rebase origin/develop
```

If conflicts occur, resolve them carefully, run tests, and continue the rebase. Do not force-push shared branches. If a force push is needed for your own rebased task branch, coordinate first and use `--force-with-lease`, never plain `--force`.

## 9. Release

When the team agrees that `develop` is ready:

1. Open a pull request from `develop` into `main`.
2. Summarize the release and verify the test suite.
3. Obtain the other developer's review.
4. Merge only after required checks and review are complete.

## Useful commands

```bash
git status
git branch
git switch develop
git pull origin develop
git fetch origin
git log --oneline --graph --decorate --all
git diff
python -m pytest
```

## Important rules

- Never commit directly to `main` or `develop` once branch protections are enabled.
- Never approve your own pull request.
- Never merge with failing required checks or unresolved review conversations.
- Never commit secrets, virtual environments, or generated cache files.
- Communicate before changing shared interfaces or project scope.
