from time import sleep
from goToPanel import goToPanel
from utils import driver
from selenium.webdriver.common.by import By

CUSTOMIZE_PAGE_XPATH = '//*[@id="page"]/header/div/div/div/div[2]/div/div'

def customize():
  goToPanel()

  sleep(2)

  messageUserButton = driver.find_element(By.XPATH, CUSTOMIZE_PAGE_XPATH)
  messageUserButton.click()

  sleep(2)


if (__name__ == '__main__'):
  customize()
  driver.close()