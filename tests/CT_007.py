

import time
from login import login
from utils import driver, UNDBClassURL
from selenium.webdriver.common.by import By

painelButtonXPath = '//*[@id="nav-drawer"]/ul/li[2]/a'
filterButtonId= 'groupingdropdown'
finishedCoursesOptionXPath = '//*[@id="yui_3_17_2_1_1661822226367_190"]/li[6]/a'


# Exibir cursos encerrados
def CT_007():
    try:
      login()
      driver.get(UNDBClassURL)

      painelButton = driver.find_element(By.XPATH, painelButtonXPath)
      painelButton.click()

      filterButton = driver.find_element(By.ID, filterButtonId)
      filterButton.click()

      finishedCoursesOption = driver.find_element(By.XPATH, finishedCoursesOptionXPath )
      finishedCoursesOption.click()

      assert 'Nenhum curso' not in driver.page_source
      

      print('CT_007: ✅ - Exibir cursos encerrados')

    except Exception as error:
      print('CT_007: ❌ - Exibir cursos encerrados')
      print(error)


if(__name__ == '__main__'):
    start_time = time.time()
    CT_007()
    time.sleep(3)
    driver.close()
    print("Done in", round(time.time() - start_time, 2), "s.")

