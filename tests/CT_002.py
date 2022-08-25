import time
from login import login
from utils import UNDBClassURL
from utils import driver
from selenium.webdriver.common.by import By

start_time = time.time()

# Exportar calendário por link clicável
def CT_002():
    try:
      exportCalendarButtonXPath = '//*[@id="yui_3_17_2_1_1661399682932_432"]'
      login()
      driver.get(UNDBClassURL + '/calendar/view.php?view=month')
    
      elem = driver.find_element(By.XPATH, exportCalendarButtonXPath)
      elem.click()
      # assert 'Av Qualis - Produto está marcado(a) para esta data' in driver.page_source

      print('CT_002: ✅ - Exportar calendário por link clicável')

    except:
      print('CT_002: ❌ - Exportar calendário por link clicável')

execution =( time.time() - start_time) * 1000

if(__name__ == '__main__'):
    CT_002()
    time.sleep(3)
    driver.close()
    print("Done in", round(execution, 4), "ms." )


