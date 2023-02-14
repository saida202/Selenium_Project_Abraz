import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://google.ca")
time.sleep(2)
driver.find_element(By.ID, 'lst-ib').send_keys('selenium')
time.sleep(2)
list_elements = driver.find_elements(By.XPATH, "//ul[@role='listbox']//li/descendant::div[@role='option']/div/span")
time.sleep(2)
print(list_elements)
time.sleep(2)
for element in list_elements:
    if element.text == "selenium webdriver":
        element.click()
    break
time.sleep(2)
driver.close()
