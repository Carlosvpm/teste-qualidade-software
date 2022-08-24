
from utils import driver 
from utils import driver, buttonAcceptCookies, UNDBClassURL
import time
from selenium.webdriver.common.by import By
def openWindow():
    driver.get(UNDBClassURL)
    driver.maximize_window()

    time.sleep(1)

    elem = driver.find_element(By.XPATH, buttonAcceptCookies)
    elem.click()
