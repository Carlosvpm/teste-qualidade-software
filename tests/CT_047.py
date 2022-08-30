import time
from login import login
from utils import driver
from selenium.webdriver.common.by import By

def CT_047():
    manualPaperXPATH = '//*[@id="module-29818"]/div/div/div[2]/div/a/span'
    login()
    
    elem = driver.find_element(By.XPATH, manualPaperXPATH)
    elem.click()


if(__name__ == '__main__'):
    CT_047()
    print('CT_047: ✅')
    driver.close()
