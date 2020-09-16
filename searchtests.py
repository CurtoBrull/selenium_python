import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class SearchTest(unittest.TestCase):
    #Prepara entorno de la prueba. 
    def setUp(self):
        self.driver = webdriver.Edge(executable_path = r'C:\Users\niven\Insync\nivend089a@gmail.com\Google Drive\Curso\Platzi\selenium_python\msedgedriver.exe')
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        driver.implicitly_wait(15)

    #Casos de prueba
    def test_search_tee(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear()

        search_field.send_keys('tee')
        search_field.submit()

    def test_search_salt_shaker(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.send_keys('salt shaker')
        search_field.submit()
        products = driver.find_elements_by_xpath('/html/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/div/h2/al')
        print(products)
        print(len(products))
        self.assertEqual(1,len(products))

    #Finalizar
    def tearDow(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
