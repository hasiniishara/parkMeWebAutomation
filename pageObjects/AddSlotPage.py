from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class AddSlotPage:

    addSlotBtn = "//*[@id='root']/div/div[2]/div/div/div[3]/div/div/a"
    addSlotPageText = "//*[@id='root']/div/div[2]/div/h4"
    addParkingSlotFieldEle = "//input[contains(@class, 'MuiOutlinedInput-input')]"
    addParkingSlotBtn = "//*[@id='root']/div/div[2]/div/button"
    successToastEle = "//div[contains(@class, 'MuiSnackbarContent-message')]"

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

    def addParkingSlot(self):
        try:
            addSlotField = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.addParkingSlotFieldEle))
            )
            addSlotField.send_keys("Hyvinkää Prisma A")
            # self.driver.find_element(By.XPATH, self.addParkingSlotFieldEle).send_keys("Hyvinkää Prisma A")
            self.driver.find_element(By.XPATH,self.addParkingSlotBtn).click()

            successToastText = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.successToastEle))
            ).text

            return successToastText
        except Exception as e:
            print(f"Error: {e}")
            return e