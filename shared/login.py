from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

usernamId = 'username'
passwordId = 'password'
sendButtonXPATH = '//*[@id="boxForm"]/div/form/div[3]/button'
UNDBClassURL = 'https://undbclassroom.undb.edu.br/'
buttonAcceptCookies = '//*[@id="freeprivacypolicy-com---nb"]/div/div[3]/button[1]'

driver = webdriver.Chrome("./utils/chromedriver.exe")
driver.get(UNDBClassURL)
driver.maximize_window()


def login():
    time.sleep(1)

    elem = driver.find_element(By.XPATH, buttonAcceptCookies)
    elem.click()

    elem = driver.find_element(By.ID, usernamId)
    elem.send_keys("002-022567")

    elem = driver.find_element(By.ID, passwordId)
    elem.send_keys("2002VINI")

    elem = driver.find_element(By.XPATH,sendButtonXPATH)
    elem.click()

if(__name__ == '__main__'):
    login()
    driver.close()
