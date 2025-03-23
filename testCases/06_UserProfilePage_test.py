import pytest
from pageObjects.UserProfilePage import UserProfilePage
from pageObjects.SigninPage import SigninPage
from utilities.customLogger import LogGen
from testCases.conftest import setup, teardown


class TestUserProfile:
    logger = LogGen.loggen()

    def setup_method(self):
        self.driver = setup()
        self.signinP = SigninPage(self.driver)
        self.userprofileP = UserProfilePage(self.driver)

    def teardown_method(self):
        teardown(self.driver)

    @pytest.mark.sanity
    def test_userprofilePage_loading(self):
        self.signinP.successUserLogin()
        userProfilePageTitle = self.userprofileP.loadUserProfilePage()
        assert "Profile" in userProfilePageTitle

