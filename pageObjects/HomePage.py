from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    homePageText = "//*[@id='root']/div/div[2]/div[1]/h1"
    realTimeCardEle = "//div[contains(@class, 'MuiCard-root') and .//h2[text()='Real-Time Availability']]"
    easyBookingCardEle = "//div[contains(@class, 'MuiCard-root') and .//h2[text()='Easy Booking']]"
    seamlessManagementCardEle = "//div[contains(@class, 'MuiCard-root') and .//h2[text()='Seamless Management']]"

    def __init__(self,driver):
        self.driver = driver

    def loadHomePage(self):
        homePageTitleText = self.driver.find_element(By.XPATH, self.homePageText).text
        return homePageTitleText

    def realTimeAvailabilityCardVisibility(self):
        try:
            realTimeCard = WebDriverWait(self.driver, 40).until(
                EC.presence_of_element_located((By.XPATH, self.realTimeCardEle))
            )
            return realTimeCard.is_displayed()
        except Exception as e:
            print(f"Error: {e}")
            return False

    def easyBookingCardVisibility(self):
        try:
            easyBookingCard = WebDriverWait(self.driver, 40).until(
                EC.presence_of_element_located((By.XPATH, self.easyBookingCardEle))
            )
            return easyBookingCard.is_displayed()
        except Exception as e:
            print(f"Error: {e}")
            return False

    def seamlessManagementCardVisibility(self):
        try:
            seamlessManagementCard = WebDriverWait(self.driver, 40).until(
                EC.presence_of_element_located((By.XPATH, self.seamlessManagementCardEle))
            )
            return seamlessManagementCard.is_displayed()
        except Exception as e:
            print(f"Error: {e}")
            return False