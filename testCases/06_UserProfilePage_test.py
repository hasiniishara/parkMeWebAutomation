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

    @pytest.mark.sanity
    def test_userProfile_lock_status(self):
        self.signinP.successUserLogin()
        self.userprofileP.loadUserProfilePage()
        profile_lock_status = self.userprofileP.checkUserProfileLockStatus()
        assert profile_lock_status,"User profile is not locked well!"

