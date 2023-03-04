import time
from venv import create

import account as account
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def test_case():
    test_browser = webdriver.Edge()
    time.sleep(10)
    test_browser.get("https://www.starbucks.com")
    test_browser.find_element(By.ID,"truste-consent-button") .click()






