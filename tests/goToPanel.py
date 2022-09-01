from time import sleep
from login import login
from utils import driver
from selenium.webdriver.common.by import By

GO_TO_PANEL_XPATH = '//*[@id="nav-drawer"]/ul/li[2]'

def goToPanel():
  login()

  sleep(2)

  panelButton = driver.find_element(By.XPATH, GO_TO_PANEL_XPATH)
  panelButton.click()


if(__name__ == '__main__'):
  goToPanel()
  driver.close()
