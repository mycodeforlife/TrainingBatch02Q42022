# python basicselenium.py
# Importing webdriver implementations
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Instance creation for firefox browser
driver = webdriver.Firefox()

# Using get method to hit url
driver.get("http://www.python.org")

# Using assert to check given text is in title or not
assert "Python" in driver.title
print("test pass")
# using find.Element method to locate elements
element = driver.find_element(By.ID, "id-search-field")
element.clear()
element.send_keys("pycon")
element.send_keys(Keys.RETURN)
assert "No such page found" not in driver.page_source
driver.quit()
#driver.close()

