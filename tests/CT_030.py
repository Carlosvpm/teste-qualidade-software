
import time
from login import login
from utils import driver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

start_time = time.time()

def CT_030():
    try:
        login()
        time.sleep(1)

        #Mostrar blocos
        blocos = driver.find_element_by_xpath('//*[@id="sidepreopen-control"]').click()
        time.sleep(1)

        #Abrir ATBAR
        ATBAR = driver.find_element_by_xpath('//*[@id="block_accessibility_launchtoolbar"]').click()
        time.sleep(2)
        
        #Selecionar texto
        texto = driver.find_element_by_xpath('//*[@id="yui_3_17_2_1_1662050591795_88"]')
        mouse = ActionChains(driver)
        mouse.double_click(texto).perform()
        #Acionar dicionário
        dicionario = driver.find_element_by_xpath('//*[@id="yui_3_17_2_1_1662050591795_87"]').click()
    
        
        print('CT_030: ✅ - Usar dicionário do ATbar de acessibilidade.')

    except:
      print('CT_023: ❌ - Usar dicionário do ATbar de acessibilidade.')

execution = (time.time() - start_time) * 1000

if(__name__ == '__main__'):
    CT_030()
    print('CT_030: ✅')
    driver.close()
    print("Done in", round(execution, 4), "ms.")

