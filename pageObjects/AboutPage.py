from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AboutPage:
    aboutPageBtn = "//*[@id='root']/div/div[1]/nav/div/div[2]/a[2]"
    aboutPageText = "//*[@id='root']/div/div[2]/div[1]/h1"

    def __init__(self,driver):
        self.driver = driver

    def loadAboutPage(self):
        self.driver.find_element(By.XPATH, self.aboutPageBtn).click()
        aboutPageTitleText = self.driver.find_element(By.XPATH, self.aboutPageText).text
        return aboutPageTitleText