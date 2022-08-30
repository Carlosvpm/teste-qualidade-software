

import time
from login import login
from utils import driver, UNDBClassURL
from selenium.webdriver.common.by import By

exportCalendarButtonXPath= '//*[@id="region-main"]/div/div/div/div/div[2]/div[1]/form'
eventsToExportInputName = 'events[exportevents]'
periodToExportInputName = 'period[timeperiod]'
getUrlCalendarButtonId = 'id_generateurl'
emailInputId = 'identifierId'
nextButtonXPath = '//*[@id="identifierNext"]/div/button'
      
calendarUrlLink = 'https://undbclassroom.undb.edu.br/calendar/export_execute.php?userid=6306&authtoken=fed57608f2d0473e6e1760245621ecc7cab32add&preset_what=all&preset_time=custom'
googleAgendaUrl = 'https://accounts.google.com/signin/v2/identifier?service=cl&passive=1209600&osid=1&continue=https%3A%2F%2Fcalendar.google.com%2Fcalendar%2Fr%3Ftab%3Dwc&followup=https%3A%2F%2Fcalendar.google.com%2Fcalendar%2Fr%3Ftab%3Dwc&flowName=GlifWebSignIn&flowEntry=ServiceLogin'

gmailAdress = 'beatrizsallesss@gmail.com'

# Adicionar calendário ao Google Agenda
def CT_003():
    try:
      login()
      driver.get(UNDBClassURL + 'calendar/view.php?view=month')

      xportCalendarButton = driver.find_element(By.XPATH, exportCalendarButtonXPath)
      xportCalendarButton.click()

      eventsToExportInput = driver.find_element(By.NAME, eventsToExportInputName)
      eventsToExportInput.click()

      periodToExportInput = driver.find_element(By.NAME, periodToExportInputName)
      periodToExportInput.click()

      urlLink = driver.find_element(By.ID, getUrlCalendarButtonId)
      urlLink.click()

      driver.get(googleAgendaUrl)

      emailInput = driver.find_element(By.ID, emailInputId)
      emailInput.send_keys(gmailAdress)

      nextButton = driver.find_element(By.XPATH, nextButtonXPath)
      nextButton.click()

      tryAgainButton = driver.find_element(By.XPATH, '//*[@id="next"]')
      tryAgainButton.click()

      nextButton = driver.find_element(By.XPATH, nextButtonXPath)
      nextButton.click()
      

      print('CT_003: ✅ - Adicionar calendário ao Google Agenda')

    except:
      print('CT_003: ❌ - Adicionar calendário ao Google Agenda')


if(__name__ == '__main__'):
    start_time = time.time()
    CT_003()
    time.sleep(3)
    driver.close()
    print("Done in", round(time.time() - start_time, 2), "s.")

