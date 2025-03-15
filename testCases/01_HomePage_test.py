import pytest

from testCases.conftest import setup, teardown
from pageObjects.HomePage import HomePage
from utilities.customLogger import LogGen

class TestHomePage:
    logger = LogGen.loggen()

    def setup_method(self):
        """Setup before each test"""
        self.driver = setup()  # Call the setup function from the separate file
        self.homeP = HomePage(self.driver)

    def teardown_method(self):
        """Teardown after each test"""
        teardown(self.driver)  # Call the teardown function from the separate file

    @pytest.mark.sanity
    def test_homePage_screen_loading(self):
        HomePageTitle= self.homeP.loadHomePage()
        assert "Welcome to ParkMe!" in HomePageTitle

    @pytest.mark.sanity
    def test_realTimeAvailability_card_visibility(self):
        available_Status = self.homeP.realTimeAvailabilityCardVisibility()
        assert available_Status, "Real-Time Availability Card is NOT visible!"

    @pytest.mark.sanity
    def test_easyBooking_card_visibility(self):
        available_Status = self.homeP.easyBookingCardVisibility()
        assert available_Status, "Easy Booking Card is NOT visible!"

    @pytest.mark.sanity
    def test_seamlessManagement_card_visibility(self):
        available_Status = self.homeP.seamlessManagementCardVisibility()
        assert available_Status, "Seamless Management Card is NOT visible!"