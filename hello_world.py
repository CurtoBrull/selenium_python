import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWorld(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
      cls.driver = webdriver.Edge(executable_path = r'C:\Users\niven\Insync\nivend089a@gmail.com\Google Drive\Curso\Platzi\selenium_python\msedgedriver.exe') # Ruta del driver
      driver = cls.driver # Indicamos el driver
      driver.implicitly_wait(10) # Esperar 10 segundos antes de la siguiente acción

  def test_hello_world(self):
      driver = self.driver # Indicamos el driver
      driver.get('https://www.platzi.com')

  def test_visit_wikipedia(self):
      driver = self.driver
      driver.get('https://es.wikipedia.org')

  @classmethod
  def tearDownClass(cls):# Indicamos que queremos cerrar ventanas de navegación después de las pruebasw
      cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'hello-word-report'))