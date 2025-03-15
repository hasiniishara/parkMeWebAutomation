from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ContactPage:
    contactPageBtn = "//*[@id='root']/div/div[1]/nav/div/div[2]/a[3]"
    contactPageText = "//*[@id='root']/div/div[2]/div[1]/h1"

    def __init__(self,driver):
        self.driver = driver

    def loadContactPage(self):
        self.driver.find_element(By.XPATH, self.contactPageBtn).click()
        contactPageTitleText = self.driver.find_element(By.XPATH, self.contactPageText).text
        return contactPageTitleText