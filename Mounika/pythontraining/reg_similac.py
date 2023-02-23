from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

req_page = webdriver.Firefox()
req_page.get("https://www.similac.com/home.html")
req_page.find_element(By.LINK_TEXT, "Register Now").click()
op_1 = req_page.find_element(By.ID, "email_id")
op_1.send_keys("chidellamounika321@gmail.com")
op_2 = req_page.find_elements()

req_page.quit()

