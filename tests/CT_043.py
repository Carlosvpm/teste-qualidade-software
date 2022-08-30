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


    assert 'Fazer login com o Google' in driver.page_source

if(__name__ == '__main__'):
    CT_043()
    print('CT_043: ✅')
    driver.close()
