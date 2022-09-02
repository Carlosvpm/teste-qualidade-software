

import time
from login import login
from utils import driver, UNDBClassURL
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

painelButtonXPath = '//*[@id="nav-drawer"]/ul/li[2]/a'
filterButtonId= 'displaydropdown'
dropdownMenuXPath = '//*[@id="yui_3_17_2_1_1661822226367_217"]/ul'
listOptionXPath = '//*[@id="yui_3_17_2_1_1661822226367_217"]/ul/li[2]/a'


# Exibir todos os cursos no formato de lista
def CT_008():
    try:
      login()
      driver.get(UNDBClassURL)
      actions =ActionChains(driver)

      painelButton = driver.find_element(By.XPATH, painelButtonXPath)
      painelButton.click()


      filterButton = driver.find_element(By.ID, filterButtonId)
      filterButton.click()

      dropdownMenu = driver.find_element(By.XPATH, dropdownMenuXPath)
      actions.move_to_element(dropdownMenu)
      actions.perform()

      listOption = driver.find_element(By.XPATH, listOptionXPath )
      listOption.click()
      
      print('CT_008: ✅ - Exibir todos os cursos no formato de lista')

    except Exception as error:
      print('CT_008: ❌ - Exibir todos os cursos no formato de lista')
      print(error)


if(__name__ == '__main__'):
    start_time = time.time()
    CT_008()
    time.sleep(3)
    driver.close()
    print("Done in", round(time.time() - start_time, 2), "s.")

