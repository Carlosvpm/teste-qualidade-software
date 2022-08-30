import time
from login import login
from utils import driver
from selenium.webdriver.common.by import By

start_time = time.time()

# Exibir conversas correspondentes ao contato inserido no menu de busca
def CT_031():
    try:

        messageMenuXPATH = '/html/body/nav/ul[2]/div[3]/a'
        searchBarXPATH = '/html/body/div[3]/div[3]/div/div[2]/div[3]/div[1]/div[1]/input'
        searchButtonXPATH = '/html/body/div[3]/div[3]/div/div[2]/div[4]/div/div/div/button'
        contact = 'GIOVANNI LUCCA FRANCA DA SILVA'


        login()
        time.sleep(1)

        # Seleciona o menu de mensagens
        elem = driver.find_element(By.XPATH, messageMenuXPATH)
        elem.click()
        time.sleep(1)

        # Seleciona a barra de pesquisa
        elem = driver.find_element(By.XPATH, searchBarXPATH)
        elem.send_keys(contact)
        time.sleep(1)

        # Clica o botão de pesquisar
        elem = driver.find_element(By.XPATH, searchButtonXPATH)
        elem.click()
        time.sleep(1)


        assert 'Nenhum resultado' not in driver.page_source

        print('CT_031: ✅ - Exibir conversas correspondentes ao contato inserido no menu de busca')

    except:

      print('CT_031: ❌ - Exibir conversas correspondentes ao contato inserido no menu de busca')

execution = (time.time() - start_time) * 1000

if(__name__ == '__main__'):
    CT_031()
    print('CT_031: ✅')
    driver.close()
    print("Done in", round(execution, 4), "ms.")
