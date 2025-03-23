from pageObjects.AddSlotPage import AddSlotPage
import pytest
from pageObjects.SigninPage import SigninPage
from utilities.customLogger import LogGen
from testCases.conftest import setup, teardown


class TestUserProfile:
    logger = LogGen.loggen()

    def setup_method(self):
        self.driver = setup()
        self.signinP = SigninPage(self.driver)
        self.addSlotP = AddSlotPage(self.driver)

    def teardown_method(self):
        teardown(self.driver)

    @pytest.mark.sanity
    def test_userprofilePage_loading(self):
        self.signinP.successUserLogin()
        addSlotPageTitle = self.addSlotP.loadAddSlotPage()
        assert "Add Parking Slot" in addSlotPageTitle

