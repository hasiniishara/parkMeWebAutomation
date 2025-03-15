import pytest
from testCases.conftest import setup, teardown
from pageObjects.AboutPage import AboutPage
from utilities.customLogger import LogGen

class TestAboutPage:
    logger = LogGen.loggen()

    def setup_method(self):
        """Setup before each test"""
        self.driver = setup()  # Call the setup function from the separate file
        self.aboutP = AboutPage(self.driver)

    def teardown_method(self):
        """Teardown after each test"""
        teardown(self.driver)  # Call the teardown function from the separate file

    @pytest.mark.sanity
    def test_aboutPage_screen_loading(self):
        AboutPageTitle= self.aboutP.loadAboutPage()
        assert "About ParkMe!" in AboutPageTitle