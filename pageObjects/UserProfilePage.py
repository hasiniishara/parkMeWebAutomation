from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class UserProfilePage:

    userProfileBtn = "//*[@id='root']/div/div[2]/div/div/div[1]/div/div/a"
    userProfilePageText = "//*[@id='root']/div/main/div/h1"
    userProfileInputEle = "//input[contains(@class, 'MuiInputBase-input')]"
    userProfileEditBtn = "//*[@id='root']/div/main/div/div[2]/button"
    userProfileLastNameEle = "lastname"
    userProfileUpdateBtn = "//*[@id='root']/div/main/div/div[2]/button[2]"
    userProfileUpdateModal = "div.MuiDialog-root.MuiModal-root"
    userProfileNoUpdateBtn = "//button[contains(text(),'No')]"
    userProfileYesUpdateBtn = "//button[contains(text(),'Yes')]"


    def __init__(self, driver):
        self.driver = driver

    def loadUserProfilePage(self):
        try:
            userProfileButton = WebDriverWait(self.driver, 40).until(
                EC.presence_of_element_located((By.XPATH, self.userProfileBtn))
            )
            userProfileButton.click()

            userProfilePageTitleText = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.userProfilePageText))
            ).text

            return userProfilePageTitleText
        except Exception as e:
            print(f"Error: {e}")
            return e

    def checkUserProfileLockStatus(self):
        try:
            InputElements = self.driver.find_elements(By.XPATH, self.userProfileInputEle)
            print("lock", len(InputElements))
            all_disabled = True
            for Inuput_Ele in InputElements:
                if not Inuput_Ele.get_attribute("disabled"):
                    all_disabled = False

            return all_disabled
        except Exception as e:
            print(f"Error: {e}")
            return e


    def checkUserProfileUnlockStatus(self):
        try:
            profileEditButton = WebDriverWait(self.driver, 40).until(
                EC.presence_of_element_located((By.XPATH, self.userProfileEditBtn))
            )
            profileEditButton.click()
            InputElements = self.driver.find_elements(By.XPATH, self.userProfileInputEle)
            print("unlock", len(InputElements))
            all_enabled = True
            for Inuput_Ele in InputElements:
                if Inuput_Ele.get_attribute("disabled"):
                    all_enabled = False

            return all_enabled
        except Exception as e:
            print(f"Error: {e}")
            return e


    def cancelUserProfileUpdate(self):
        try:
            profileEditButton = WebDriverWait(self.driver, 40).until(
                EC.presence_of_element_located((By.XPATH, self.userProfileEditBtn))
            )
            profileEditButton.click()
            self.driver.find_element(By.ID, self.userProfileLastNameEle).send_keys(Keys.CONTROL + "a")
            self.driver.find_element(By.ID, self.userProfileLastNameEle).send_keys(Keys.DELETE)
            self.driver.find_element(By.ID, self.userProfileLastNameEle).send_keys("Isharaa")
            self.driver.find_element(By.XPATH, self.userProfileUpdateBtn).click()

            modal = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, self.userProfileUpdateModal))
            )

            no_button = self.driver.find_element(By.XPATH, self.userProfileNoUpdateBtn)
            no_button.click()
            userProfilePageTitleText = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.userProfilePageText))
            ).text

            return userProfilePageTitleText
        except Exception as e:
            print(f"Error: {e}")
            return e

    def updateUserProfile(self):
        try:
            profileEditButton = WebDriverWait(self.driver, 40).until(
                EC.presence_of_element_located((By.XPATH, self.userProfileEditBtn))
            )
            profileEditButton.click()
            self.driver.find_element(By.ID, self.userProfileLastNameEle).send_keys(Keys.CONTROL + "a")
            self.driver.find_element(By.ID, self.userProfileLastNameEle).send_keys(Keys.DELETE)
            self.driver.find_element(By.ID, self.userProfileLastNameEle).send_keys("Isharaa")
            self.driver.find_element(By.XPATH, self.userProfileUpdateBtn).click()

            modal = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, self.userProfileUpdateModal))
            )

            yes_button = self.driver.find_element(By.XPATH, self.userProfileYesUpdateBtn)
            yes_button.click()

            profileEditButton = WebDriverWait(self.driver, 40).until(
                EC.presence_of_element_located((By.XPATH, self.userProfileEditBtn))
            )
            return profileEditButton.is_displayed()
        except Exception as e:
            print(f"Error: {e}")
            return e

