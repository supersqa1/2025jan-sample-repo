
import pytest

pytestmark = pytest.mark.regression

@pytest.fixture(scope="class")
def my_setup_teardown():
    # add setup steps here
    # like creating a test data
    name = "admas"
    yield name
    # add teardown steps here
    # like delete test data
    pass


# @pytest.mark.usefixtures("my_setup_teardown")
class TestMyRegstrationTests:


    @pytest.mark.smoke
    @pytest.mark.abc1
    def test_verify_valid_registration(self, my_setup_teardown):
        
        print("*** Running test to valiate registration.")
        print(my_setup_teardown)
        print("I am new a line")


    @pytest.mark.tcid1
    @pytest.mark.regression
    @pytest.mark.prodok
    def test_verify_invalid_registration(self):
        print("Running invalid registration.")