import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(2)
driver.find_element(By.NAME,"username").send_keys("Admin")
time.sleep(2)
driver.find_element(By.NAME,"password").send_keys("admin123")
time.sleep(2)
driver.find_element(By.XPATH,'//button[@type="submit"]').click()
time.sleep(2)
#find_elements
list_liens=driver.find_elements(By.TAG_NAME,"a")
print(len(list_liens))
time.sleep(2)
print("text du premier lien:",list_liens[3].text)
for link in list_liens:
    print(link.text)
time.sleep(2)

driver.close()
