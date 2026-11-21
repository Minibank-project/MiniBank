"""Smoke tests for the initial MiniBank project scaffold."""


def test_banking_package_can_be_imported():
    import banking

    assert banking.__doc__ is not None
