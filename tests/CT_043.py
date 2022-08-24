from utils import driver
from selenium.webdriver.common.by import By
import time
from utils import driver, buttonAcceptCookies
from openWindow import openWindow

def CT_043():
    openWindow()
    
    loginGoogleXPATH = '//*[@id="boxForm"]/div/div/div/a'
    
    elem = driver.find_element(By.XPATH, loginGoogleXPATH)
    elem.click()
    

if(__name__ == '__main__'):
    CT_043()
    time.sleep(1)
    driver.close()
