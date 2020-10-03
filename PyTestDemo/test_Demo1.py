# Any pytest file should start with test_ or end with _test
# pytest methods name should start with test
# any code should be wrapped in method only
# -k stands for menthod names execution
# -s log in output
# -v log more info metadata
# you can mark (tag) tests and then run with -m option
# CMD> py.test -k Card -v -s
# CMD> py.test filename


import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram(setup):
    print("Hello")


def test_secondProgram():
    print("Hi")


def testCressBrowser(crossBrowser):
    # print(crossBrowser)
    print(crossBrowser[0])
    print(crossBrowser[1])