import pytest
from selenium import webdriver
from utilities.readProperties import ReadConfig

@pytest.fixture(scope='function',autouse=True)
def setup(request):
    baseUrl = ReadConfig.getApplicationURL()
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(baseUrl)
    request.cls.driver = driver

    def teardown():
        driver.quit()

    request.addfinalizer(teardown)



# def setup():
#     baseUrl = ReadConfig.getApplicationURL()
#     """Setup function to initialize WebDriver"""
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get(baseUrl)
#     return driver
#
# def teardown(driver):
#     """Teardown function to quit WebDriver"""
#     driver.quit()
