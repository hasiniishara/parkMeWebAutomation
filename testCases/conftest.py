from selenium import webdriver
from utilities.readProperties import ReadConfig

def setup():
    baseUrl = ReadConfig.getApplicationURL()
    """Setup function to initialize WebDriver"""
    print("\n[Setup] Launching Chrome Browser...")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(baseUrl)
    return driver

def teardown(driver):
    """Teardown function to quit WebDriver"""
    print("\n[Teardown] Closing Chrome Browser...")
    driver.quit()
