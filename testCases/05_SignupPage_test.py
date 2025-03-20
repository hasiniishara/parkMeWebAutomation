import pytest
from testCases.conftest import setup, teardown
from pageObjects.SignupPage import SignupPage
from utilities.customLogger import LogGen


class TestSignupPage:

    logger =  LogGen.loggen()

    def setup_method(self):
        self.driver = setup()
        self.signupP = SignupPage(self.driver)

    def teardown_method(self):
        teardown(self.driver)

    @pytest.mark.sanity
    def test_signupPage_screen_loading(self):
        signupPageTitle = self.signupP.loadSignupPage()
        assert "Sign Up" in signupPageTitle

    @pytest.mark.sanity
    def test_success_user_registration(self):
        self.signupP.successUserRegistration()

