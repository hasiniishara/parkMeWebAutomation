import pytest
from testCases.conftest import setup, teardown
from pageObjects.ContactPage import ContactPage
from utilities.customLogger import LogGen

class TestContactPage:
    logger = LogGen.loggen()

    def setup_method(self):
        """Setup before each test"""
        self.driver = setup()  # Call the setup function from the separate file
        self.contactP = ContactPage(self.driver)

    def teardown_method(self):
        """Teardown after each test"""
        teardown(self.driver)  # Call the teardown function from the separate file

    @pytest.mark.sanity
    def test_contactPage_screen_loading(self):
        ContactPageTitle= self.contactP.loadContactPage()
        assert "Contact Us" in ContactPageTitle