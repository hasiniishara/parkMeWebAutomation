import pytest
from pageObjects.AboutPage import AboutPage
from utilities.customLogger import LogGen

@pytest.mark.usefixtures("setup")
class TestAboutPage:
    logger = LogGen.loggen()

    def setup_method(self):
        self.aboutP = AboutPage(self.driver)

    @pytest.mark.sanity
    def test_aboutPage_screen_loading(self):
        AboutPageTitle= self.aboutP.loadAboutPage()
        assert "About ParkMe!" in AboutPageTitle