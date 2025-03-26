from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class UserProfilePage:

    userProfileBtn = "//*[@id='root']/div/div[2]/div/div/div[1]/div/div/a"
    userProfilePageText = "//*[@id='root']/div/main/div/h1"
    userProfileInputEle = "//input[contains(@class, 'Mui-disabled')]"

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
        InputElements = self.driver.find_elements(By.XPATH, self.userProfileInputEle)

        all_disabled = True
        for Inuput_Ele in InputElements:
            if not Inuput_Ele.get_attribute("disabled"):
                all_disabled = False

        return all_disabled