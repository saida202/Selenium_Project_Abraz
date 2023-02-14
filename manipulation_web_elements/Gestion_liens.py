import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(2)
list_Link=driver.find_elements(By.TAG_NAME,"a")
print("le nombre de liens sur la page est : ",len(list_Link))
time.sleep(2)
for link in list_Link:
    print(link.text)
    print(link.get_attribute("href"))
driver.close()