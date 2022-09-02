

import time
from login import login
from utils import driver, UNDBClassURL
from selenium.webdriver.common.by import By

painelButtonXPath = '//*[@id="nav-drawer"]/ul/li[2]/a'
filterButtonId= 'groupingdropdown'
notStartedCoursesOptionXPath = '//*[@id="yui_3_17_2_1_1661822226367_181"]/ul/li[5]'


# Exibir cursos não iniciados
def CT_005():
    try:
      login()
      driver.get(UNDBClassURL)

      painelButton = driver.find_element(By.XPATH, painelButtonXPath)
      painelButton.click()

      filterButton = driver.find_element(By.ID, filterButtonId)
      filterButton.click()

      notStartedCoursesOption = driver.find_element(By.XPATH, notStartedCoursesOptionXPath)
      notStartedCoursesOption.click()

      assert 'Nenhum curso' not in driver.page_source
      

      print('CT_005: ✅ - Exibir cursos não iniciados')

    except Exception as error:
      print('CT_005: ❌ - Exibir cursos não iniciados')
      print(error)


if(__name__ == '__main__'):
    start_time = time.time()
    CT_005()
    time.sleep(3)
    driver.close()
    print("Done in", round(time.time() - start_time, 2), "s.")

