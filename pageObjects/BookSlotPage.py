from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BookSlotPage:

    bookSlotBtn = "//*[@id='root']/div/div[2]/div/div/div[2]/div/div/a"
    fetchToastEle = "//p[contains(@class, 'css-1fitlit')]"
    deleteBtn = "//button[contains(text(), 'Delete')]"
    slotDeleteModal = "//div[contains(@class, 'MuiPaper-root')]"
    slotDeleteNoBtn = "//button[contains(text(),'Cancel')]"
    slotDeleteYesBtn = "/html/body/div[2]/div[3]/div/div[2]/button[2]"

    def __init__(self,driver):
        self.driver = driver

    def loadBookSlotPage(self):
        try:
            bookSlotButton = WebDriverWait(self.driver, 40).until(
                EC.presence_of_element_located((By.XPATH, self.bookSlotBtn))
            )
            bookSlotButton.click()
            fetchToastText = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.fetchToastEle))
            ).text
            return fetchToastText
        except Exception as e:
            print(f"Error: {e}")
            return e

    def cancelDeleteSlot(self):
        try:
            deleteButtons = WebDriverWait(self.driver, 40).until(
                EC.presence_of_all_elements_located((By.XPATH, self.deleteBtn))
            )
            print(len(deleteButtons))
            if len(deleteButtons) > 0:
                deleteButtons[0].click()
                modal = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, self.slotDeleteModal))
                )
                no_button = self.driver.find_element(By.XPATH, self.slotDeleteNoBtn)
                no_button.click()
            else:
                print("No parking slots are available")
        except Exception as e:
            print(f"Error: {e}")
            return e

    def deleteSlot(self):
        try:
            deleteButtons = WebDriverWait(self.driver, 40).until(
                EC.presence_of_all_elements_located((By.XPATH, self.deleteBtn))
            )
            if len(deleteButtons) > 0:
                deleteButtons[0].click()
                modal = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, self.slotDeleteModal))
                )
                yes_button = self.driver.find_element(By.XPATH, self.slotDeleteYesBtn)
                yes_button.click()
            else:
                print("No parking slots are available")
        except Exception as e:
            print(f"Error: {e}")
            return e