from selenium.webdriver.common.by import By
import time
from utils import driver, buttonAcceptCookies, UNDBClassURL, USERNAME, PASSWORD

usernamElementId = 'username'
passwordElementId = 'password'
sendButtonXPATH = '//*[@id="boxForm"]/div/form/div[3]/button'





def login():
   
    driver.get(UNDBClassURL)
    driver.maximize_window()

    time.sleep(1)

    elem = driver.find_element(By.XPATH, buttonAcceptCookies)
    elem.click()

    elem = driver.find_element(By.ID, usernamElementId)
    elem.send_keys(USERNAME)

    elem = driver.find_element(By.ID, passwordElementId)
    elem.send_keys(PASSWORD)

    elem = driver.find_element(By.XPATH,sendButtonXPATH)
    elem.click()

if(__name__ == '__main__'):
     login()
     driver.close()
