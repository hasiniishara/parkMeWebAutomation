from pageObjects.AddSlotPage import AddSlotPage
import pytest
from pageObjects.SigninPage import SigninPage
from utilities.customLogger import LogGen

@pytest.mark.usefixtures("setup")
class TestUserProfile:
    logger = LogGen.loggen()

    def setup_method(self):
        self.signinP = SigninPage(self.driver)
        self.addSlotP = AddSlotPage(self.driver)

    @pytest.mark.sanity
    def test_uaddSlotPage_loading(self):
        self.signinP.successUserLogin()
        addSlotPageTitle = self.addSlotP.loadAddSlotPage()
        assert "Add Parking Slot" in addSlotPageTitle

    @pytest.mark.regression
    def test_add_ParkingSlot(self):
        self.signinP.successUserLogin()
        self.addSlotP.loadAddSlotPage()
        successMessage = self.addSlotP.addParkingSlot()
        assert "Parking slot added successfully!" in successMessage