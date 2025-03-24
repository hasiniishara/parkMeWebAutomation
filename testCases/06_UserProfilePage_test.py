import pytest
from pageObjects.UserProfilePage import UserProfilePage
from pageObjects.SigninPage import SigninPage
from utilities.customLogger import LogGen

@pytest.mark.usefixtures("setup")
class TestUserProfile:
    logger = LogGen.loggen()

    def setup_method(self):
        self.signinP = SigninPage(self.driver)
        self.userprofileP = UserProfilePage(self.driver)

    @pytest.mark.sanity
    def test_userprofilePage_loading(self):
        self.signinP.successUserLogin()
        userProfilePageTitle = self.userprofileP.loadUserProfilePage()
        assert "Profile" in userProfilePageTitle

