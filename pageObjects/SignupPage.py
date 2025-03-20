from selenium.webdriver.common.by import By
from utilities import ExcelUtils



class SignupPage:

    path = ".//Data/UserRegistrationDetails.xlsx"

    signupPageBtn = "//*[@id='root']/div/div[1]/nav/div/div[2]/a[5]"
    signupPageText = "//*[@id='root']/div/div[2]/div/h5"
    userFirstNameFieldElement = "firstname"
    userLastNameFieldElement = "lastname"
    userNameFieldElement = "username"
    userEmailFieldElement = "email"
    userPWFieldElement = "password"
    userRegisterBtn = "//*[@id='root']/div/div[2]/div/form/button"

    def __init__(self, driver):
        self.driver = driver

    def loadSignupPage(self):
        self.driver.find_element(By.XPATH, self.signupPageBtn).click()
        signupPageTitleText = self.driver.find_element(By.XPATH, self.signupPageText).text
        return signupPageTitleText

    def successUserRegistration(self):
        self.driver.find_element(By.XPATH, self.signupPageBtn).click()
        self.rows = ExcelUtils.getRowCount(self.path, 'Sheet1')
        print("Number of Rows", self.rows)

        for r in range(2, self.rows + 1):
            self.firstName = ExcelUtils.readData(self.path, 'Sheet1', r, 1)
            self.lastName = ExcelUtils.readData(self.path, 'Sheet1', r, 2)
            self.userName = ExcelUtils.readData(self.path, 'Sheet1', r, 3)
            self.userEmail = ExcelUtils.readData(self.path, 'Sheet1', r, 4)
            self.userPw = ExcelUtils.readData(self.path, 'Sheet1', r, 5)

            if not all([self.firstName, self.lastName, self.userName, self.userEmail, self.userPw]):
                print(f"Skipping row {r} due to missing data")
                continue

            self.driver.find_element(By.ID, self.userFirstNameFieldElement).send_keys(self.firstName)
            self.driver.find_element(By.ID, self.userLastNameFieldElement).send_keys(self.lastName)
            self.driver.find_element(By.ID, self.userNameFieldElement).send_keys(self.userName)
            self.driver.find_element(By.ID, self.userEmailFieldElement).send_keys(self.userEmail)
            self.driver.find_element(By.ID, self.userPWFieldElement).send_keys(self.userPw)

            self.driver.find_element(By.XPATH, self.userRegisterBtn).click()