from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class AddSlotPage:

    addSlotBtn = "//*[@id='root']/div/div[2]/div/div/div[3]/div/div/a"
    addSlotPageText = "//*[@id='root']/div/div[2]/div/h4"

    def __init__(self, driver):
        self.driver = driver

    def loadAddSlotPage(self):
        try:
            addSlotButton = WebDriverWait(self.driver, 40).until(
                EC.presence_of_element_located((By.XPATH, self.addSlotBtn))
            )
            addSlotButton.click()

            addSlotPageTitleText = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.addSlotPageText))
            ).text

            return addSlotPageTitleText
        except Exception as e:
            print(f"Error: {e}")
            return e