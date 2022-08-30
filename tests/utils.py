from selenium import webdriver
import platform

from tests.CT_042 import PASSWORD

UNDBClassURL = 'https://undbclassroom.undb.edu.br/'

buttonAcceptCookies = '//*[@id="freeprivacypolicy-com---nb"]/div/div[3]/button[1]'

driver = webdriver.Chrome() if platform.system() == 'Darwin' else webdriver.Chrome("./utils/chromedriver.exe")


USERNAME='USERNAME'
PASSWORD ='PASSWORD'