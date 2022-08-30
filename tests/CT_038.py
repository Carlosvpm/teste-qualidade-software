from ast import keyword
import time
from login import login
from utils import driver
from selenium.webdriver.common.by import By

start_time = time.time()

# Entrada com a data no “advanced search”
def CT_038():
    try:

        emailMenuXPATH = '/html/body/nav/ul[2]/div[4]/div[1]'
        emailInboxXPATH = '/html/body/nav/ul[2]/div[4]/div[2]/div[2]/div/div/a[1]'
        searchButtonXPATH = '/html/body/div[3]/div[2]/div/div/section/div/div/div/div/form/div[1]/div[2]/span[5]'
        advancedSearchButtonXPATH = '/html/body/div[3]/div[2]/div/div/section/div/div/div/div/form/div[6]/div[4]/div/div[2]/div[2]/span'
        dateInputBarXPATH = '/html/body/div[3]/div[2]/div/div/section/div/div/div/div/form/div[6]/div[4]/div/div[2]/div[3]/div[4]/span/span'
        selectedDateXPATH = '/html/body/div[7]/div/div/div/div/div/div[2]/table/tbody/tr[1]/td[7]'
        submitButtonXPATH = '/html/body/div[3]/div[2]/div/div/section/div/div/div/div/form/div[6]/div[4]/div/div[3]/span/button[1]'

        login()
        time.sleep(1)

        # Seleciona o menu de emails
        elem = driver.find_element(By.XPATH, emailMenuXPATH)
        elem.click()
        time.sleep(1)
        
        # Seleciona a caixa de entrada
        elem = driver.find_element(By.XPATH, emailInboxXPATH)
        elem.click()
        time.sleep(1)

        # Clica o botão Buscar
        elem = driver.find_element(By.XPATH, searchButtonXPATH)
        elem.click()
        time.sleep(1)

        # Clica no botão "Advanced Search"
        elem = driver.find_element(By.XPATH, advancedSearchButtonXPATH)
        elem.click()
        time.sleep(1)

        # Clica no formulário da data
        elem = driver.find_element(By.XPATH, dateInputBarXPATH)
        elem.click()
        time.sleep(1)

        # Seleciona a data de 01/08
        elem = driver.find_element(By.XPATH, selectedDateXPATH)
        elem.click()
        time.sleep(1)

        # Clica no botão Buscar
        elem = driver.find_element(By.XPATH, submitButtonXPATH)
        elem.click()
        time.sleep(1)

        assert 'Sem e-mails para visualizar. Mostrar mensagens recentes' not in driver.page_source

        print('CT_038: ✅ - Entrada com a data no “advanced search”')

    except:
      print('CT_038: ❌ - Entrada com a data no “advanced search”')

execution = (time.time() - start_time) * 1000

if(__name__ == '__main__'):
    CT_038()
    print('CT_038: ✅')
    driver.close()
    print("Done in", round(execution, 4), "ms.")
