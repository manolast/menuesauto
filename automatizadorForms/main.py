import time
import csv

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select




options = Options();
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

driver.get("https://login.ordereat.com.uy/generate_registration")
driver.maximize_window()
time.sleep(4)
maillogin = driver.find_element(By.XPATH, '//*[@id="normal_login_username"]')
passlogin = driver.find_element(By.XPATH, '//*[@id="normal_login_password"]')

maillogin.send_keys(input('email:'))
passlogin.send_keys(input('contrasena:'))

time.sleep(5)

buttonlogin = driver.find_element(By.XPATH, '//*[@id="normal_login"]/div[3]/div/div/div/button')
buttonlogin.click()

time.sleep(10)

nombre_pais = input('De que pais es la cantina: ')
nombre_cantina = input('Nombre de la cantina: ')


dropdown_pais = driver.find_element(By.XPATH, '/html/body/div[1]/div/section/div/div/div/div/div/div/div[1]/div/div/span[1]/input')
dropdown_pais.send_keys(nombre_pais)
dropdown_pais.send_keys(Keys.ENTER)

time.sleep(10)


# try:
tr_cantina = driver.find_element(By.XPATH, f"//td[contains(text(),'{nombre_cantina}')]/ancestor::tr")

    #boton iniciar sesion
boton_sesion = driver.find_element(By.XPATH, f"//td[contains(text(),'{nombre_cantina}')]/ancestor::tr/td/div/button[5]")
boton_sesion.click()

hamb_button = driver.find_element(By.XPATH, '//*[@id="root"]/header/button')
hamb_button.click()
boton_menus = driver.find_element(By.XPATH, '//a[@href="/menus"]')
boton_menus.click()
time.sleep(3)
# except: #NoSuchElementException:
#     # If the TD element is not found, click the button that takes to the next page
#     next_page_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/section/div/div/div/div/div/ul/li[7]/button')
#     next_page_button.click()

# with open('csvprueba.csv', 'r') as archivo_csv:
#     lector_csv = csv.DictReader(archivo_csv)
#     for fila in lector_csv:
#         buscar = driver.find_element(By.XPATH, "//input[@class='gLFyf']")
#         buscar.send_keys(fila['email'])
#         time.sleep(5)
#         buscar.send_keys(Keys.ENTER)
#         time.sleep(5)


nuevo_menu = driver.find_element(By.XPATH, '//*[@id="root"]/div/section/div/button')
nuevo_menu.click()
input_titulo = driver.find_element(By.XPATH, '//*[@id="name"]')
input_descrip = driver.find_element(By.XPATH, '//*[@id="description"]')
input_fecha = driver.find_element(By.XPATH, '//*[@id="displayDate"]')
input_precio = driver.find_element(By.XPATH, '//*[@id="price"]')

input_titulo.send_keys('sandwich')
input_descrip.send_keys('de jamon y queso')
input_fecha.send_keys('2023-05-07')
input_precio.send_keys(500)

time.sleep(10)

guardar_menu = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/div/div/form/div[2]/div[5]/div[2]/button[2]')
guardar_menu.click()
