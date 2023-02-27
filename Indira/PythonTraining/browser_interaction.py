import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def send_keys(param):
    pass


def test_case():
    test_browser = webdriver.Firefox()
    time.sleep(30)
    test_browser.get("https://www.instacart.com")
    test_browser.find_element(By.CLASS_NAME, "css-utfnc").click()
    test_browser.find_element(By.CLASS_NAME, "css-16hj45o").send_keys("indoochowdary@gmail.com")
    test_browser.find_element(By.ID, "id-vkjo9n").send_keys("Indi1224")
    test_browser.find_element(By.CLASS_NAME, "css-1i23zk9").click()
    # search_element.send_keys("candle" + Keys.ENTER)

    """page_title = test_browser.title
    print(page_title)
    if "Amazon.com" in page_title:
        print("Test pass")
    else:
        print("Test Failed")
    test_browser.quit()"""




