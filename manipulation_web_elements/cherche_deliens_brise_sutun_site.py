#import selenium
import time
import requests
import requests as requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(2)
list_Link=driver.find_elements(By.TAG_NAME,"a")
compteur=0
for link in list_Link:
    url=link.get_attribute("href")
    try:
        response=requests.head(url)
    except:
        None
    if response.status_code>=400:
        print(url," est un lien brise ")
        compteur=compteur+1
    else:
        print(url," le lien est valide ")
print("le nombre de liens brise esr : ",compteur)
driver.close()
#lien brise veut dire un lien avec erreur par ex 404 si c est cote client ou 500 cote serveur