import time
import csv
import pwinput
import sys


from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException

options = Options();
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

driver.get("https://login.ordereat.com.uy/generate_registration")
driver.maximize_window()
driver.implicitly_wait(5)
maillogin = driver.find_element(By.XPATH, '//*[@id="normal_login_username"]')
passlogin = driver.find_element(By.XPATH, '//*[@id="normal_login_password"]')

maillogin.send_keys(input('Email: '))
passlogin.send_keys(pwinput.pwinput(prompt='Contraseña: '))
passlogin.send_keys(Keys.ENTER)

nombre_pais = input('De que pais es la cantina: ')
nombre_cantina = input('Nombre de la cantina: ')
csv_file = input('Nombre del Archivo: ')

dropdown_pais = driver.find_element(By.XPATH, '/html/body/div[1]/div/section/div/div/div/div/div/div/div[1]/div/div/span[1]/input')
dropdown_pais.send_keys(nombre_pais)
dropdown_pais.send_keys(Keys.ENTER)

time.sleep(3)

cantina_found = False
while not cantina_found:
    # Buscar boton cantina
    try:
        button_sesion = driver.find_element(By.XPATH, f"//td[contains(text(),'{nombre_cantina}')]/ancestor::tr/td/div/button[5]")
        button_sesion.click()
        cantina_found = True
    except NoSuchElementException:
        try:
            # Si no se encuentra el boton de inicio de sesion para la cantina
            button_nextpage = driver.find_element(By.XPATH, '//*[@id="root"]/div/section/div/div/div/div/div/ul/li[@title="Página siguiente"]/button')
            if not button_nextpage.is_enabled():
                # Si esta disabled es que se llego a la ultima pagina y no se encontro la cantina
                sys.exit('No se pudo encontrar la cantina. Checkea los datos de país y nombre de la cantina')

            button_nextpage.click()
            # Esperar que cargue pagina
            driver.implicitly_wait(1)
        except Exception:
            sys.exit('Ocurrio un error')
            break

hamb_button = driver.find_element(By.XPATH, '//*[@id="root"]/header/button')
hamb_button.click()
button_menus = driver.find_element(By.XPATH, '//a[@href="/menus"]')
button_menus.click()
driver.implicitly_wait(5)

with open(f"{csv_file}", 'r') as archivo_csv:
    lector_csv = csv.DictReader(archivo_csv)
    for fila in lector_csv:
        #clickea para crear nuevo menu
        nuevo_menu = driver.find_element(By.XPATH, '//*[@id="root"]/div/section/div/button')
        nuevo_menu.click()
        #identifica inputs
        input_titulo = driver.find_element(By.XPATH, '//*[@id="name"]')
        input_descrip = driver.find_element(By.XPATH, '//*[@id="description"]')
        input_fecha = driver.find_element(By.XPATH, '//*[@id="displayDate"]')
        input_precio = driver.find_element(By.XPATH, '//*[@id="price"]')
        #llena inputs con los datos del csv
        input_titulo.send_keys(fila['titulo'])
        input_descrip.send_keys(fila['descripcion'])
        input_fecha.send_keys(fila['fecha'])
        input_precio.send_keys(fila['precio'])
        time.sleep(1)
        #guarda el menu apretando enter
        input_precio.send_keys(Keys.ENTER)
