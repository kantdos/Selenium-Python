import pytest

# conf file to generalize fixture and make it available to all the test cases


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("I will be executing at last")


@pytest.fixture()
def dataLoad():
    print("User profile data is being created")
    return ["Ravi", "Kant", "kant.dos@gmail.com"]

# Data driven and parametrization can be done with return statement in tuple format
# When you define fixture scope to class only, it will run once before class is initiated and at the end


@pytest.fixture(params=[("Chrome","Ravi1"),("FireFox","Ravi2"),("IE","Ravi3")])
def crossBrowser(request):
    return request.param