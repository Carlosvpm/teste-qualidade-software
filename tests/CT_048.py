import time
from login import login
from utils import driver
from selenium.webdriver.common.by import By

def CT_047():
    manualCaseXPATH = '//*[@id="module-29817"]/div/div/div[2]/div/a/span'
    login()
    
    elem = driver.find_element(By.XPATH, manualCaseXPATH)
    elem.click()


if(__name__ == '__main__'):
    CT_047()
    time.sleep(2)
    driver.close()
