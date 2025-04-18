from pageObjects.BookSlotPage import BookSlotPage
import pytest
from pageObjects.SigninPage import SigninPage
from utilities.customLogger import LogGen

@pytest.mark.usefixtures("setup")
class TestUserProfile:
    logger = LogGen.loggen()

    def setup_method(self):
        self.signinP = SigninPage(self.driver)
        self.bookSlotP = BookSlotPage(self.driver)

    @pytest.mark.sanity
    def test_bookslotPage_loading(self):
        self.signinP.successUserLogin()
        fetchText = self.bookSlotP.loadBookSlotPage()
        assert "Parking slots fetched successfully!" in fetchText

    @pytest.mark.regression
    def test_cancel_slot_delete(self):
        self.signinP.successUserLogin()
        self.bookSlotP.loadBookSlotPage()
        self.bookSlotP.cancelDeleteSlot()


