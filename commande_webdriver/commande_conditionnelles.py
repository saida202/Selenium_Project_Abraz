import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("http://omayo.blogspot.com")
time.sleep(2)
case_a_cocher=driver.find_element(By.ID,'checkbox1').is_selected()
print(case_a_cocher)
time.sleep(2)
check_enabled_element = driver.find_element(By.ID,'but2').is_enabled()
print(check_enabled_element)
time.sleep(2)
check_displayed_element = driver.find_element(By.ID,'hbutton').is_displayed()
print(check_displayed_element)
driver.close()