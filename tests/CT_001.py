import time
from login import login
from utils import driver
from selenium.webdriver.common.by import By

# Teste de 01 a 10 feitos por Beatriz Salles

start_time = time.time()
# Exibir datas de atividades das disciplinas em curso no calendário
def CT_001():
    try:
      calendarXPATH = '//*[@id="nav-drawer"]/ul/li[3]/a'
      login()
    
      elem = driver.find_element(By.XPATH, calendarXPATH)
      elem.click()
      assert 'Av Qualis - Produto está marcado(a) para esta data' in driver.page_source

      print('CT_001: ✅ - Exibir datas de atividades das disciplinas em curso no calendário')

    except Exception as error:
      print('CT_001: ❌ - Exibir datas de atividades das disciplinas em curso no calendário')
      print(error)

execution =( time.time() - start_time) * 1000

if(__name__ == '__main__'):
    start_time = time.time()
    CT_001()
    time.sleep(3)
    driver.close()
    print("Done in", round(time.time() - start_time, 2), "s.")


