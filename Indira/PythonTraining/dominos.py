import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def test_case2():
    test_browser = webdriver.Firefox()
    time.sleep(5)
    test_browser.get("https://www.Dominos.com")


# Click on the "Sign up" link
    test_browser.find_element(By.CSS_SELECTOR, ".css-137gprl") .click()
    test_browser.find_element(By.LINK_TEXT, "JOIN NOW") .click()
    time.sleep(10)

# Fill in the required fields on the registration form
    test_browser.find_element(By.CSS_SELECTOR, "label.loyalty-offer__form__label:nth-child(1) > input:nth-child(2)").send_keys("indira")
    test_browser.find_element(By.CSS_SELECTOR, "label.loyalty-offer__form__label:nth-child(2) > input:nth-child(2)").send_keys("vadlamudi")
    test_browser.find_element(By.NAME, "email").send_keys("indoochowdary@gmail.com")
    #test_browser.find_element(By.CSS_SELECTOR, "label.loyalty - offer__form__label: nth - child(3) > input:nth - child(2)").send_keys("indoochowdary+@gmail.com")
    test_browser.find_element(By.CSS_SELECTOR, "label.loyalty-offer__form__label:nth-child(4) > input:nth-child(2)").send_keys("indoochowdary+@gmail.com")
    test_browser.find_element(By.ID, "loyalty-offer__form__phone").send_keys("6176530433")
    test_browser.find_element(By.CSS_SELECTOR, "label.loyalty-offer__form__label:nth-child(6) > input:nth-child(2)").send_keys("+indi1225")
    test_browser.find_element(By.CSS_SELECTOR, "label.loyalty-offer__form__label:nth-child(7) > input:nth-child(2)").send_keys("+indi1225")
    #test_browser.find_element(By.ID, "loyalty-offer__form__email-list-signup").click()
    test_browser.find_element(By.XPATH, " /html/body/div[3]/div[2]/div/section/div/form/div[2]/button").click()








