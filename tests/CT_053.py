import time
from login import login
from utils import driver
from selenium.webdriver.common.by import By


def CT_053():

    login()

    elem = driver.find_element(
        By.NAME, 'q')
    elem.send_keys('Professores')

    elem = driver.find_element(
        By.XPATH, '//*[@id="region-main"]/div/div/div/div[2]/div/form/div/div/button')

    elem.click()


if(__name__ == '__main__'):
    CT_053()
    time.sleep(2)
    print('CT_053: ✅')
    driver.close()
