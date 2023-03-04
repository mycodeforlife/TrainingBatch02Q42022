import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def test_case1():
    test_browser = webdriver.Firefox()
    time.sleep(10)
#open the instacart website
    test_browser.get("https://www.instacart.com")
#click on signup button
    test_browser.find_element(By.CLASS_NAME, "css-1sakx1").click()
    test_browser.find_element(By.CLASS_NAME, "css-16hj45o").send_keys("annesrinithya@gmail.com")
    test_browser.find_element(By.CLASS_NAME, "css-1i23zk9").click()
    test_browser.find_element(By.CSS_SELECTOR, "#id-30mnfn").send_keys("srinithya")



