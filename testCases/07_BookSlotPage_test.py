from pageObjects.BookSlotPage import BookSlotPage
import pytest
from pageObjects.SigninPage import SigninPage
from utilities.customLogger import LogGen
from testCases.conftest import setup, teardown


class TestUserProfile:
    logger = LogGen.loggen()

    def setup_method(self):
        self.driver = setup()
        self.signinP = SigninPage(self.driver)
        self.bookSlotP = BookSlotPage(self.driver)

    def teardown_method(self):
        teardown(self.driver)

    @pytest.mark.sanity
    def test_bookslotPage_loading(self):
        self.signinP.successUserLogin()
        self.bookSlotP.loadBookSlotPage()

