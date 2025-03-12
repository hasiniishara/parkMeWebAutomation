import pytest

from testCases.conftest import setup, teardown
from pageObjects.HomePage import HomePage
from utilities.customLogger import LogGen

class TestSearch:
    logger = LogGen.loggen()

    def setup_method(self):
        """Setup before each test"""
        self.driver = setup()  # Call the setup function from the separate file

    def teardown_method(self):
        """Teardown after each test"""
        teardown(self.driver)  # Call the teardown function from the separate file

    @pytest.mark.sanity
    def test_homePage_screen_loading(self):
        self.homeP = HomePage(self.driver)
        HomePageTitle= self.homeP.loadHomePage()
        assert "Welcome to ParkMe!" in HomePageTitle