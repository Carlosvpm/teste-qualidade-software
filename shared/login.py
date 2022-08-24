from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

usernamElementId = 'username'
passwordElementId = 'password'
sendButtonXPATH = '//*[@id="boxForm"]/div/form/div[3]/button'
UNDBClassURL = 'https://undbclassroom.undb.edu.br/'
buttonAcceptCookies = '//*[@id="freeprivacypolicy-com---nb"]/div/div[3]/button[1]'

USERNAME = 'username'
PASSWORD = 'password'

driver = webdriver.Chrome("./utils/chromedriver.exe")
driver.get(UNDBClassURL)
driver.maximize_window()


def login():
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
