from selenium.webdriver.common.by import By
from Funciones.Funciones import FuncionesGlobales

class PaginaLogin:
    def __init__(self, driver):
        self.driver = driver

    def login_master(self, url, usuario, password, t):
        f = FuncionesGlobales(self.driver)
        f.navegar(url, t)
        f.ingresar_texto(By.XPATH, usuario, t, "//input[contains(@id, 'user-name')]", )
        f.ingresar_texto(By.ID, password, t, "password")
        f.click(By.ID, t, "login-button")
        f.salida()