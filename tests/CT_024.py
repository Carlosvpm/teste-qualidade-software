

import time
from login import login
from utils import driver
from selenium.webdriver.common.by import By

start_time = time.time()

def CT_024():
    try:
        login()
        time.sleep(1)

        #Mostrar blocos
        blocos = driver.find_element_by_xpath('//*[@id="sidepreopen-control"]').click()
        time.sleep(1)

        #Abrir ATBAR
        ATBAR = driver.find_element_by_xpath('//*[@id="block_accessibility_launchtoolbar"]').click()
        time.sleep(2)

        #Usar Word Prediction
        WordPrediction = driver.find_element_by_xpath('//*[@id="yui_3_17_2_1_1662050591795_82"]').click()
        
        #Digitar texto na barra de pesquisa
        texto = driver.find_element_by_xpath('//*[@id="searchinput-6310e155570f96310e15525a0435"]').click()
        texto.send_keys('test')
        time.sleep(1)
        
        assert 'Nenhuma palavra sugerida' not in driver.page_source
        
        print('CT_024: ✅ - Usar Word Prediction.')

    except:
      print('CT_024: ❌ -Usar Word Prediction..')

execution = (time.time() - start_time) * 1000

if(__name__ == '__main__'):
    CT_024()
    print('CT_024: ✅')
    driver.close()
    print("Done in", round(execution, 4), "ms.")

