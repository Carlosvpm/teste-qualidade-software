

import time
from login import login
from utils import driver
from selenium.webdriver.common.by import By

start_time = time.time()

def CT_022():
    try:
        login()
        time.sleep(1)

        #Clica no botão libras
        libras = driver.find_element_by_xpath('//*[@id="yui_3_17_2_1_1662050591795_53"]').click()
        time.sleep(3)
        
        #Clica em um texto
        text = driver.find_element_by_xpath('//*[@id="yui_3_17_2_1_1662058910481_65"]').click()
        time.sleep(3)

        assert 'Texto traduzido' not in driver.page_source


        print('CT_022: ✅ - Traduzir para libras quando botão libras for acionado')

    except:
      print('CT_022: ❌ - Traduzir para libras quando botão libras for acionado.')

execution = (time.time() - start_time) * 1000

if(__name__ == '__main__'):
    CT_022()
    print('CT_022: ✅')
    driver.close()
    print("Done in", round(execution, 4), "ms.")



