import pytest
from testCases.conftest import setup, teardown
from utilities.customLogger import LogGen
from pageObjects.SigninPage import SigninPage
from utilities.readProperties import ReadConfig


class TestSigninPage:
    logger = LogGen.loggen()

    def setup_method(self):
        self.driver = setup()
        self.signinP= SigninPage(self.driver)
        self.userName = ReadConfig.getUserName()
        self.userPw = ReadConfig.getUserPassword()

    def teardown_method(self):
        teardown(self.driver)

    @pytest.mark.sanity
    def test_signinPage_screen_loading(self):
        signinPageTitle = self.signinP.loadSigninPage()
        assert "Sign In" in signinPageTitle

    @pytest.mark.sanity
    def test_success_user_login(self):
        self.signinP.successUserLogin(self.userName,self.userPw)

