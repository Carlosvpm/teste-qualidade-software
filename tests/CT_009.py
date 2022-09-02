

import time
from login import login
from utils import driver, UNDBClassURL
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

painelButtonXPath = '//*[@id="nav-drawer"]/ul/li[2]/a'
filterButtonId= 'displaydropdown'
dropdownMenuXPath = '//*[@id="yui_3_17_2_1_1661822226367_217"]/ul'
summaryOptionXPath = '//*[@id="yui_3_17_2_1_1662080990433_186"]'
firstCourseXPath = '//*[@id="yui_3_17_2_1_1662080990433_812"]/div[1]'

class element_has_css_class(object):
  def __init__(self, locator, css_class):
    self.locator = locator
    self.css_class = css_class

  def __call__(self, driver):
    element = driver.find_element(*self.locator) 
    if self.css_class in element.get_attribute("class"):
        return element
    else:
        return False


# Exibir todos os cursos no formato de resumo
def CT_009():
    try:
      login()
      driver.get(UNDBClassURL)

      painelButton = driver.find_element(By.XPATH, painelButtonXPath)
      painelButton.click()


      filterButton = driver.find_element(By.ID, filterButtonId)
      filterButton.click()

      wait = WebDriverWait(driver, 3)
      summaryOption = wait.until(EC.visibility_of_element_located((By.XPATH, summaryOptionXPath )))
      summaryOption.click()

      isSummary = wait.until(element_has_css_class((By.XPATH, firstCourseXPath), "course-summaryitem "))
      print(isSummary)
      if(isSummary):
        print('CT_009: ✅ - Exibir todos os cursos no formato de resumo')

    except Exception as error:
      print('CT_009: ❌ - Exibir todos os cursos no formato de resumo')
      print(error)


if(__name__ == '__main__'):
    start_time = time.time()
    CT_009()
    time.sleep(3)
    driver.close()
    print("Done in", round(time.time() - start_time, 2), "s.")

