

import time
from login import login
from utils import driver, UNDBClassURL
from selenium.webdriver.common.by import By

searchInputXPath = '/html/body/div[3]/div[2]/div/div/section/div/div/div/div[2]/div/form/div/input'
submitButtonXPath= '//*[@id="region-main"]/div/div/div/div[2]/div/form/div/div/button'
search = 'teste'


# Buscar cursos em meus cursos
def CT_010():
    try:
      login()
      driver.get(UNDBClassURL)

      searchInput = driver.find_element(By.XPATH, searchInputXPath)
      searchInput.send_keys(search)


      submitButton = driver.find_element(By.XPATH, submitButtonXPath)
      submitButton.click()


      print('CT_010: ✅ - Buscar cursos em meus cursos')
        

    except Exception as error:
      print('CT_010: ❌ - Buscar cursos em meus cursos')
      print(error)


if(__name__ == '__main__'):
    start_time = time.time()
    CT_010()
    time.sleep(3)
    driver.close()
    print("Done in", round(time.time() - start_time, 2), "s.")

