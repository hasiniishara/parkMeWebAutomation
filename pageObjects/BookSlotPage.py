from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BookSlotPage:

    bookSlotBtn = "//*[@id='root']/div/div[2]/div/div/div[2]/div/div/a"

    def __init__(self,driver):
        self.driver = driver

    def loadBookSlotPage(self):
        try:
            bookSlotButton = WebDriverWait(self.driver, 40).until(
                EC.presence_of_element_located((By.XPATH, self.bookSlotBtn))
            )
            bookSlotButton.click()
        except Exception as e:
            print(f"Error: {e}")
            return e