import pytest
from utilities.customLogger import LogGen
from pageObjects.SigninPage import SigninPage

@pytest.mark.usefixtures("setup")
class TestSigninPage:
    logger = LogGen.loggen()

    def setup_method(self):
        self.signinP= SigninPage(self.driver)

    @pytest.mark.sanity
    def test_signinPage_screen_loading(self):
        signinPageTitle = self.signinP.loadSigninPage()
        assert "Sign In" in signinPageTitle

    @pytest.mark.sanity
    def test_success_user_login(self):
        self.signinP.successUserLogin()

