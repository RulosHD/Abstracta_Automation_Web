from pages.web_base_page import web_base_page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

class opencart_page(web_base_page):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.title_portal = "//*[@id='logo']/h1/a"
        self.barra_busqueda = "//*[@id='search']/input"
        self.title_busqueda = "//*[@id='content']/h1"
        self.lista_items = "//div[@id='content']/div[3]/div"
        self.title_producto = "//*[@id='content']/div[1]/div[2]/h1"
        self.boton_agregar_carrito = "//*[@id='button-cart']"
        self.text_confirmacion_agregar_producto = "//div[@id='product-product']/div[1]/a"
        self.boton_carrito_compra = "//*[@id='cart']/button"
        self.div_carrito_compra_desplegado = "//*[@id='cart']/ul"
        self.title_primer_producto_carrito_compra = "//*[@id='content']/form/div/table/tbody/tr/td[2]/a"
        self.boton_view_cart = "//*[@id='cart']/ul/li[2]/div/p/a[1]/strong"
        self.boton_remover_producto = "//*[@id='content']/form/div/table/tbody/tr/td[4]/div/span/button[2]"
        self.text_remover_producto = "(//div[@id='content']/p)[1]"

    def ingreso_a_portal(self, url):
        try: 
            self.driver.maximize_window()
            self.driver.get(url)
        except Exception as e:
            raise Exception("Error al ingresar al portal: ", str(e))
        
    def get_text_title(self):
        try:
            super().wait_until_element_is_visible(self.title_portal)
            element = self.driver.find_element(By.XPATH, self.title_portal)  
            return element.text 
        except Exception as e:
            raise Exception("Error al obtener el título: ", str(e))
    
    def send_keys_barra_busqueda(self, texto):
        try:
            super().wait_until_element_is_visible(self.barra_busqueda)
            element = self.driver.find_element(By.XPATH, self.barra_busqueda)
            element.send_keys(texto)
            element.send_keys(Keys.ENTER)
        except Exception as e:
            raise Exception("Error al ingresar texto en la barra de búsqueda: ", str(e))

    def get_text_title_busqueda(self):
        try:
            super().wait_until_element_is_visible(self.title_busqueda)
            element = self.driver.find_element(By.XPATH, self.title_busqueda)  
            return element.text 
        except Exception as e:
            raise Exception("Error al obtener el título de la búsqueda: ", str(e))
        
    def click_primer_item(self):
        try:
            super().wait_until_element_is_visible(self.lista_items)
            elemento = self.driver.find_element(By.XPATH,"//div[@id='content']/div[3]/div[1]")
            elemento.click()
        except Exception as e:
            raise Exception("Error al seleccionar el primer item: ", str(e))
        
    def click_agregar_item_carrito(self, element):
        try:
            super().wait_until_element_is_clickable(element)
            element.click()
        except Exception as e:
            raise Exception("Error al seleccionar el botón Agregar al carrito: ", str(e))
    
    def get_text_title_producto(self):
        try:
            super().wait_until_element_is_visible(self.title_producto)
            element = self.driver.find_element(By.XPATH, self.title_producto)  
            return element.text 
        except Exception as e:
            raise Exception("Error al obtener el título del producto: ", str(e))
    
    def click_boton_agregar_a_carrito(self):
        try:
            super().wait_until_element_is_visible(self.boton_agregar_carrito)
            self.driver.find_element(By.XPATH, self.boton_agregar_carrito).click()
        except Exception as e:
            raise Exception("Error al seleccionar el botón Agregar al carrito: ", str(e))

    def get_text_label_agregar_producto(self):
        try:
            super().wait_until_element_is_visible(self.text_confirmacion_agregar_producto)
            element = self.driver.find_element(By.XPATH, self.text_confirmacion_agregar_producto)  
            return element.text 
        except Exception as e:
            raise Exception("Error al obtener el texto de confirmación de agregar producto: ", str(e))
    
    def click_boton_carrito_compra(self):
        try:
            super().wait_until_element_is_visible(self.boton_carrito_compra)
            self.driver.find_element(By.XPATH, self.boton_carrito_compra).click()
        except Exception as e:
            raise Exception("Error al seleccionar el botón Continuar compra: ", str(e))

    def is_displayed_carrito_compra(self):
        try:
            super().wait_until_element_is_visible(self.div_carrito_compra_desplegado)
            element = self.driver.find_element(By.XPATH, self.div_carrito_compra_desplegado)
            return super().is_displayed(element, 30)
        except Exception as e:
            raise Exception("Error al verificar si el carrito de compra está desplegado: ", str(e))
    
    def get_text_primer_producto_carrito(self):
        try:
            super().wait_until_element_is_visible(self.title_primer_producto_carrito_compra)
            element = self.driver.find_element(By.XPATH, self.title_primer_producto_carrito_compra)
            return element.text
        except Exception as e:
            raise Exception("Error" + str(e))
    
    def click_boton_view_cart(self):
        try:
            super().wait_until_element_is_visible(self.boton_view_cart)
            self.driver.find_element(By.XPATH, self.boton_view_cart).click()
        except Exception as e:
            raise Exception("Error al seleccionar el botón Ver carrito: ", str(e))

    def click_boton_remover_producto(self):
        try:
            super().wait_until_element_is_visible(self.boton_remover_producto)
            self.driver.find_element(By.XPATH, self.boton_remover_producto).click()
        except Exception as e:
            raise Exception("Error al seleccionar el botón Remover producto: ", str(e))
        
    def get_text_remover_producto(self):
        try:
            sleep(3)
            super().wait_until_element_is_visible(self.text_remover_producto)
            element = self.driver.find_element(By.XPATH, self.text_remover_producto)  
            return element.text
        except Exception as e: 
            raise Exception("Error al obtener el texto de confirmación de remover producto: ", str(e))