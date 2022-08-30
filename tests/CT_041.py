from utils import driver
from selenium.webdriver.common.by import By
import time
from utils import driver, buttonAcceptCookies, UNDBClassURL

usernamElementId = 'username'
passwordElementId = 'password'
sendButtonXPATH = '//*[@id="boxForm"]/div/form/div[3]/button'
PASSWORD = 'PASSWORD'
USERNAME = 'USERNAME'

def CT_041():

    driver.get(UNDBClassURL)
    driver.maximize_window()

    time.sleep(1)

    elem = driver.find_element(By.XPATH, buttonAcceptCookies)
    elem.click()

    elem = driver.find_element(By.ID, usernamElementId)
    #USUÁRIO INVÁLIDO
    elem.send_keys(USERNAME)

    elem = driver.find_element(By.ID, passwordElementId)
    elem.send_keys(PASSWORD)

    elem = driver.find_element(By.XPATH, sendButtonXPATH)
    elem.click()

    elem = driver.find_element(By.ID, 'loginerrormessage')
    assert 'Nome de usuário ou senha errados. Por favor tente outra vez.' in driver.page_source or elem.text


if(__name__ == '__main__'):
    CT_041()
    print('CT_041: ✅')
    driver.close()
