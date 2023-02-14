#import selenium
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)
#on lui demande ici de nous donner le nombre de ligne dans le tableau html sur la page internet
nombre_de_lignes=driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr")
print(len(nombre_de_lignes))
#ici on a demande le nombre de collones
nombre_de_colones=driver.find_elements(By.XPATH,"//table[@name='BookTable']//th")
print(len(nombre_de_colones))
#ici on lui demander de recuperer la valeur d une cellule de la table avec XPATH
val_cel=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[3]/td[1]")
print(val_cel.text)
#exercice :recuperer toutes les donnees du tableau
nb_de_lignes=len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr"))
nb_de_colones=len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//th"))
time.sleep(2)
val_head=driver.find_elements(By.XPATH, "//table[@name='BookTable']//th")
for h in range(1,len(val_head)+1):
    data_head=driver.find_element(By.XPATH, "//table[@name='BookTable']//th["+str(h)+"]").text
    print(data_head)
time.sleep(2)
for r in range(2, nb_de_lignes+ 1):
    for c in range(1,nb_de_colones+1):
        valeur_cell=driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(r)+"]/td["+str(c)+"]").text
        print(valeur_cell,end="    ")
    print()
time.sleep(2)
#exercice
#ici on lui demande de chercher ce que l auteur Amit a comme livre et c quoi le prix
for r in range(2, nb_de_lignes+ 1):
        auteur=driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(r)+"]/td[2]").text
        if auteur =='Amit':
            prix=driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(r)+"]/td[4]").text
            nom_livre =driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(r)+"]/td[1]").text
            print(auteur, "********",nom_livre,"********",prix)

driver.close()
