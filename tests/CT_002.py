

import time
from login import login
from utils import driver, UNDBClassURL
from selenium.webdriver.common.by import By

#Exportar calendário por link clicável
def CT_002():
    try:
      login()
      driver.get(UNDBClassURL + 'calendar/view.php?view=month')

      exportCalendarButtonXPath= '//*[@id="region-main"]/div/div/div/div/div[2]/div[1]/form'
      eventsToExportInputName = 'events[exportevents]'
      periodToExportInputName = 'period[timeperiod]'
      getUrlCalendarButtonId = 'id_generateurl'
      getUrlCalendarElementXPath = '//*[@id="region-main"]/div/div/div/div/div'
      
      xportCalendarButton = driver.find_element(By.XPATH, exportCalendarButtonXPath)
      xportCalendarButton.click()

      eventsToExportInput = driver.find_element(By.NAME, eventsToExportInputName)
      eventsToExportInput.click()

      periodToExportInput = driver.find_element(By.NAME, periodToExportInputName)
      periodToExportInput.click()

      urlLink = driver.find_element(By.ID, getUrlCalendarButtonId)
      urlLink.click()
      
      urlCalendar = driver.find_element(By.XPATH, getUrlCalendarElementXPath)
      urlCalendar.click()

      print('CT_002: ✅ - Exportar calendário por link clicável')

    except Exception as error:
      print('CT_002: ❌ - Exportar calendário por link clicável')
      print(error)


if(__name__ == '__main__'):
    start_time = time.time()
    CT_002()
    time.sleep(3)
    driver.close()
    print("Done in", round(time.time() - start_time, 2), "s.")

