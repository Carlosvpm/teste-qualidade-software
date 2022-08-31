from time import sleep
from goToPanel import goToPanel
from utils import driver
from selenium.webdriver.common.by import By

def message():
  goToPanel()

  sleep(2)

  messageUserButton = driver.find_element(By.ID, 'message-user-button')
  messageUserButton.click()


if (__name__ == '__main__'):
  message()
  driver.close()