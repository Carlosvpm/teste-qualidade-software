

import time
from login import login
from utils import driver, UNDBClassURL
from selenium.webdriver.common.by import By

calendarUrl = UNDBClassURL + 'calendar/view.php?view=month'
newEventButtonXPath= '//*[@id="yui_3_17_2_1_1661476325143_432"]'
eventNameInputId = 'id_name'
saveButtonId = 'yui_3_17_2_1_1661476325143_602'
eventName = 'Novo Evento Teste'


# Adicionar novo evento no calendário
def CT_004():
    try:
      login()
      driver.get(calendarUrl)

      newEventButton = driver.find_element(By.XPATH, newEventButtonXPath)
      newEventButton.click()

      eventNameInput = driver.find_element(By.ID, eventNameInputId)
      eventNameInput.send_keys(eventName)

      saveButton = driver.find_element(By.ID, saveButtonId)
      saveButton.click()

      assert eventName in driver.page_source
      

      print('CT_004: ✅ - Adicionar novo evento no calendário')

    except Exception as error:
      print('CT_004: ❌ - Adicionar novo evento no calendário')
      print(error)


if(__name__ == '__main__'):
    start_time = time.time()
    CT_004()
    time.sleep(3)
    driver.close()
    print("Done in", round(time.time() - start_time, 2), "s.")

