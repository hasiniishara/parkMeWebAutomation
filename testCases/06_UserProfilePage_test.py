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

    @pytest.mark.sanity
    def test_userProfile_unlock_status(self):
        self.signinP.successUserLogin()
        self.userprofileP.loadUserProfilePage()
        profile_unlock_status = self.userprofileP.checkUserProfileUnlockStatus()
        assert profile_unlock_status, "User profile is not unlock for edit"

    @pytest.mark.sanity
    def test_cancel_userProfile_update(self):
        self.signinP.successUserLogin()
        self.userprofileP.loadUserProfilePage()
        userProfilePageTitle = self.userprofileP.cancelUserProfileUpdate()
        assert "Profile" in userProfilePageTitle

    @pytest.mark.sanity
    def test_update_userProfile(self):
        self.signinP.successUserLogin()
        self.userprofileP.loadUserProfilePage()
        edit_btn_available_Status = self.userprofileP.updateUserProfile()
        assert edit_btn_available_Status, "Edit button is NOT visible!"

