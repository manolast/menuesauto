import time
import csv

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



options = Options();
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

driver.get("https://login.ordereat.com.uy/generate_registration")
driver.maximize_window()
time.sleep(4)

nombre_pais = input('De que pais es la cantina')
nombre_cantina = input('Nombre de la cantina')

#encontrar y clickear pais
dropdown_pais = driver.find_element(By.XPATH, '//*[@id="root"]/div/section/div/div/div/div/div/div/div[1]/div')
dropdown_pais.click
selector_pais = driver.find_element(By.XPATH, f"//div[@title={nombre_pais} and ancestor::div[4][preceding-sibling::div[@id='rc_select_4_list']]]")
selector_pais.click


try:
    tr_cantina = driver.find_element(By.XPATH, f"//td[contains(text(),'{nombre_cantina}')]/ancestor::tr")

    #boton iniciar sesion
    boton_sesion = tr_cantina.find_element(By.XPATH, './td//button[descendant::span[contains(@class, 'anticon-login')]]')
    boton_sesion.click()
except: #NoSuchElementException:
    # If the TD element is not found, click the button that takes to the next page
    next_page_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/section/div/div/div/div/div/ul/li[7]/button')
    next_page_button.click()

# with open('csvprueba.csv', 'r') as archivo_csv:
#     lector_csv = csv.DictReader(archivo_csv)
#     for fila in lector_csv:
#         buscar = driver.find_element(By.XPATH, "//input[@class='gLFyf']")
#         buscar.send_keys(fila['email'])
#         time.sleep(5)
#         buscar.send_keys(Keys.ENTER)
#         time.sleep(5)