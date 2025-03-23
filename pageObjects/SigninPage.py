from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig


class SigninPage:
    signinPageBtn = "//*[@id='root']/div/div[1]/nav/div/div[2]/a[4]"
    signinPageText = "//*[@id='root']/div/div[2]/div/h5"
    userNameFieldElement = "username"
    userPWFieldElement = "password"
    userLoginBtn = "//*[@id='root']/div/div[2]/div/div[2]/form/button"

    def __init__(self,driver):
        self.driver = driver
        self.userName = ReadConfig.getUserName()
        self.userPw = ReadConfig.getUserPassword()

    def loadSigninPage(self):
        self.driver.find_element(By.XPATH, self.signinPageBtn).click()
        signinPageTitleText= self.driver.find_element(By.XPATH, self.signinPageText).text
        return signinPageTitleText

    def successUserLogin(self):
        self.driver.find_element(By.XPATH, self.signinPageBtn).click()
        self.driver.find_element(By.ID, self.userNameFieldElement).send_keys(self.userName)
        self.driver.find_element(By.ID, self.userPWFieldElement).send_keys(self.userPw)
        self.driver.find_element(By.XPATH, self.userLoginBtn).click()


