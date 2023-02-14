import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(2)
placeholder_text=driver.find_element(By.XPATH,'//input[@name="username"]').get_attribute("placeholder")
print(placeholder_text)
time.sleep(2)
list_liens=driver.find_elements(By.TAG_NAME,'a')
for lien in list_liens:
    print(lien.get_attribute("href"))
time.sleep(2)
driver.close()