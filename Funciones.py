import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class FuncionesGlobales:
    def __init__(self, driver):
        self.driver = driver

    def tiempo(self, t):
        time.sleep(t)

    def navegar(self, url, t):
        self.driver.get(url)
        print("Página cargada: ", url)
        time.sleep(t)

    def existe(self, tipo, t, selector):
        try:
            elem = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((tipo, selector)))
            self.driver.execute_script("arguments[0].scrollIntoView();", elem)
            print(f"Se encontró el elemento: \"{selector}\".")
            time.sleep(t)
            return True
        except TimeoutException as ex:
            print(ex.msg)
            print(f"No se encontró el elemento: \"{selector}\".")
            return False

    def ingresar_texto(self, tipo, texto, t, *args):
        if len(args) == 0:
            print("Error: Faltan argumentos.")
        for selector in args:
            try:
                elem = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((tipo, selector)))
                self.driver.execute_script("arguments[0].scrollIntoView();", elem)
                elem.clear()
                elem.send_keys(texto)
                print(f"Escribiendo en el elemento: \"{selector}\", el texto: \"{texto}\".")
                time.sleep(t)
            except TimeoutException as ex:
                print(ex.msg)
                print(f"No se encontró el elemento: \"{selector}\".")

    def click(self, tipo, t, *args):
        if len(args) == 0:
            print("Error: Faltan argumentos.")
        for selector in args:
            try:
                elem = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((tipo, selector)))
                self.driver.execute_script("arguments[0].scrollIntoView();", elem)
                elem.click()
                print(f"Dando click en el elemento: \"{selector}\".")
                time.sleep(t)
            except TimeoutException as ex:
                print(ex.msg)
                print(f"No se encontró el elemento: \"{selector}\".")

    def select(self, tipo, tipo_option, dato, t, *args):
        if len(args) == 0:
            print("Error: Faltan argumentos.")
        for selector in args:
            try:
                elem = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((tipo, selector)))
                self.driver.execute_script("arguments[0].scrollIntoView();", elem)
                if tipo_option == "text":
                    Select(elem).select_by_visible_text(dato)
                elif tipo_option == "index":
                    Select(elem).select_by_index(dato)
                elif tipo_option == "value":
                    Select(elem).select_by_value(dato)
                else:
                    print("Error: tipo de select no válido.")

                print(f"Seleccionando la opción: \"{dato}\", en el elemento: \"{selector}\", por tipo: \"{tipo_option}\".")
                time.sleep(t)
            except TimeoutException as ex:
                print(ex.msg)
                print(f"No se encontró el elemento: \"{selector}\".")

    def upload(self, tipo, ruta, t, *args):
        if len(args) == 0:
            print("Error: Faltan argumentos.")
        for selector in args:
            try:
                elem = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((tipo, selector)))
                self.driver.execute_script("arguments[0].scrollIntoView();", elem)
                elem.send_keys(ruta)
                print(f"Cargando el archivo: \"{ruta}\", en el elemento: \"{selector}\".")
                time.sleep(t)
            except TimeoutException as ex:
                print(ex.msg)
                print(f"No se encontró el elemento: \"{selector}\".")

    def salida(self):
        print("La prueba ha finalizado con éxito.")