import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def test_case():
    test_browser = webdriver.Firefox()
    time.sleep(10)
    test_browser.get("https://www.instacart.com")
    test_browser.find_element(By.CLASS_NAME, "css-utfnc").click()
    test_browser.find_element(By.CLASS_NAME, "css-16hj45o").send_keys("annesrinithya@gmail.com")
    test_browser.findElement(By.linkText("Sign Up")).click();.send_keys("srinithya")
    test_browser.find_element(By.CLASS_NAME, "css-1i23zk9").click()

