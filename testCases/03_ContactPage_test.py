import pytest
from pageObjects.ContactPage import ContactPage
from utilities.customLogger import LogGen

@pytest.mark.usefixtures("setup")
class TestContactPage:
    logger = LogGen.loggen()

    def setup_method(self):
        self.contactP = ContactPage(self.driver)

    @pytest.mark.sanity
    def test_contactPage_screen_loading(self):
        ContactPageTitle= self.contactP.loadContactPage()
        assert "Contact Us" in ContactPageTitle