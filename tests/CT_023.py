

import time
from login import login
from utils import driver
from selenium.webdriver.common.by import By

start_time = time.time()

def CT_023():
    try:
        login()
        time.sleep(1)

        #Clica no botão libras
        libras = driver.find_element_by_xpath('//*[@id="yui_3_17_2_1_1662050591795_53"]').click()
        time.sleep(3)

        #Clica em fechar
        fechar = driver.find_element_by_xpath('//*[@id="yui_3_17_2_1_1662050591795_77"]').click()
        time.sleep(1)


        print('CT_023: ✅ - Fechar o painel de libras.')

    except:
      print('CT_023: ❌ - Fechar o painel de libras..')

execution = (time.time() - start_time) * 1000

if(__name__ == '__main__'):
    CT_023()
    print('CT_023: ✅')
    driver.close()
    print("Done in", round(execution, 4), "ms.")

