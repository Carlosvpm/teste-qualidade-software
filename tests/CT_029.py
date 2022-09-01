

import time
from login import login
from utils import driver
from selenium.webdriver.common.by import By

start_time = time.time()

def CT_029():
    try:
        login()
        time.sleep(1)

        #Seleciona o menu
        menu = driver.find_element_by_xpath('//*[@id="action-menu-toggle-1"]').click()
        time.sleep(1)

        #Clica em preferências
        preferencias = driver.find_element_by_xpath('//*[@id="action-menu-1-menu"]/a[6]').click()
        time.sleep(2)
        
        #Clica em preferências de mensagens
        preferencias_msg = driver.find_element_by_xpath('//*[@id="region-main"]/div/div/div/div/div/div[1]/div/div/div/div[8]/a').click()
        time.sleep(2)
        
        #Selecionar apenas meus contatos
        mensagens = driver.find_element_by_xpath(' //*[@id="yui_3_17_2_1_1662058687387_31"]').click()

    

        print('CT_029: ✅ - Ajustar preferências de mensagens.')

    except:
      print('CT_029: ❌ - Ajustar preferências de mensagens.')

execution = (time.time() - start_time) * 1000

if(__name__ == '__main__'):
    CT_029()
    print('CT_029: ✅')
    driver.close()
    print("Done in", round(execution, 4), "ms.")

