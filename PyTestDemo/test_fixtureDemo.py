import pytest

# fixtures are used ti setup and tear down methods for test cases


@pytest.mark.usefixtures("setup")
class TestExample:
    def test_fixtureDemo1(self):
        print("I will be executing steps in fixture method 1")

    def test_fixtureDemo2(self):
        print("I will be executing steps in fixture method 2")

    def test_fixtureDemo3(self):
        print("I will be executing steps in fixture method 3")

    def test_fixtureDemo4(self):
        print("I will be executing steps in fixture method 4")