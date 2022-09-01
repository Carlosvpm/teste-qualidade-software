

import time
from login import login
from utils import driver
from selenium.webdriver.common.by import By

start_time = time.time()

def CT_021():
    try:
        login()
        time.sleep(1)

        #Seleciona o menu
        menu = driver.find_element_by_xpath('//*[@id="action-menu-toggle-1"]').click()
        time.sleep(1)

        #Clica em notas
        notas = driver.find_element_by_xpath('//*[@id="action-menu-1-menu"]/a[4]').click()
        time.sleep(1)

        assert 'Nenhuma nota encontrada' not in driver.page_source

        print('CT_021: ✅ - Acessar notas.')

    except:
      print('CT_021: ❌ - Acessar notas.')

execution = (time.time() - start_time) * 1000

if(__name__ == '__main__'):
    CT_021()
    print('CT_021: ✅')
    driver.close()
    print("Done in", round(execution, 4), "ms.")




