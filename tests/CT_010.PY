from time import sleep
from login import login
from utils import RETURN, driver
from selenium.webdriver.common.by import By


SEARCH_QUERY = 'farmacologia'

def search():
  login()

  sleep(2)

  searchInput = driver.find_element(By.NAME, 'q')
  searchInput.send_keys(SEARCH_QUERY)
  searchInput.send_keys(RETURN)

if (__name__ == '__main__'):
  search()
  driver.close()
