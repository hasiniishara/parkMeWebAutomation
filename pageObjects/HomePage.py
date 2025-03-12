from selenium import webdriver
from selenium.webdriver.common.by import By

class HomePage:
    homePageText = "//*[@id='root']/div/div[2]/div[1]/h1"

    def __init__(self,driver):
        self.driver = driver

    def loadHomePage(self):
        homePageTitleText = self.driver.find_element(By.XPATH, self.homePageText).text
        return homePageTitleText
