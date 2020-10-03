import pytest


@pytest.mark.smoke
def test_firstProgram():
    message = "Hello"
    assert message == "Hi", "Test failed because string does not match"

@pytest.mark.xfail
def test_cCardTest():
    message = "Card"
    assert message == "Card"


