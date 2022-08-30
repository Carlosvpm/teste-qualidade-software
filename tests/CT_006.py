

import time
from login import login
from utils import driver, UNDBClassURL
from selenium.webdriver.common.by import By

painelButtonXPath = '//*[@id="nav-drawer"]/ul/li[2]/a'
filterButtonId= 'groupingdropdown'
startedCoursesOptionId = 'yui_3_17_2_1_1661822226367_189'


# Exibir somente cursos em andamento
def CT_006():
    try:
      login()
      driver.get(UNDBClassURL)

      painelButton = driver.find_element(By.XPATH, painelButtonXPath)
      painelButton.click()

      filterButton = driver.find_element(By.ID, filterButtonId)
      filterButton.click()

      startedCoursesOption = driver.find_element(By.ID, startedCoursesOptionId)
      startedCoursesOption.click()

      assert 'ES05AN-2022.2 - SEGURANÇA E AUDITORIA DE SISTEMAS' not in driver.page_source
      

      print('CT_006: ✅ - Exibir somente cursos em andamento')

    except:
      print('CT_006: ❌ - Exibir somente cursos em andamento')


if(__name__ == '__main__'):
    start_time = time.time()
    CT_006()
    time.sleep(3)
    driver.close()
    print("Done in", round(time.time() - start_time, 2), "s.")

