import pytest
from pageObjects.SignupPage import SignupPage
from utilities.customLogger import LogGen

@pytest.mark.usefixtures("setup")
class TestSignupPage:

    logger =  LogGen.loggen()

    def setup_method(self):
        self.signupP = SignupPage(self.driver)

    @pytest.mark.sanity
    def test_signupPage_screen_loading(self):
        signupPageTitle = self.signupP.loadSignupPage()
        assert "Sign Up" in signupPageTitle

    @pytest.mark.sanity
    def test_success_user_registration(self):
        self.signupP.successUserRegistration()

