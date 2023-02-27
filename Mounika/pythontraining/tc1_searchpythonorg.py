import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class PythonOrgSearch(unittest.TestCase):

  def setUp(self):
      self.driver = webdriver.Firefox()

  def Test_Python_Org_Search(self):
      driver = self.driver
      driver.get("http://www.python.org")
      self.assertIn("Python", driver.title)
      element = driver.find_element(By.ID, "id-search-field")
      element.send_keys("Pycon")
      element.send_keys("Keys.RETURN")
      self.assertNotIn("File not found", driver.page_source)

  def tearDown(self):
      self.driver.close()

if __name__ == "__main__":
    unittest.main()

