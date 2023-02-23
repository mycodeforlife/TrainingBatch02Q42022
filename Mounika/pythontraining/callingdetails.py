<input type="text" name="passwd" id="passwd-id" />


element = driver.find_element(By.ID, "passwd-id")
element = driver.find_element(By.NAME, "passwd")
element = driver.find_element(By.XPATH,"//input[@id = 'passwd-id']")
element = driver.find_element(By.CSS_SELECTOR,'input#passwd-id')
element.send_keys("some text")
element.send_keys("some other text", Keys.ARROW_DOWN)
element.clear()
\
