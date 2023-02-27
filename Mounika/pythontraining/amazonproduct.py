import pytest


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_case1():
    home_page = webdriver.Firefox()
    home_page.implicitly_wait(30)
    home_page.get("https://www.amazon.com/")
    search_1 = home_page.find_element(By.ID, "twotabsearchtextbox")
    search_1.send_keys("Bright Starts Oball Shaker Rattle Toy, Ages Newborn +", Keys.ENTER)
    home_page.find_element(By.LINK_TEXT, "Bright Starts Oball Shaker Rattle Toy, Ages Newborn +").click()
    home_page.find_element(By.ID, "add-to-cart-button").click()
    home_page.find_element(By.LINK_TEXT, "Go to Cart").click()
    print('Item added to cart successfully')
    home_page.close()



def test_case2():
    home_page = webdriver.Firefox()
    home_page.implicitly_wait(30)
    home_page.get("https://www.ebay.com/")
    search_1 = home_page.find_element(By.ID, "twotabsearchtextbox")
    search_1.send_keys("Bright Starts Oball Shaker Rattle Toy, Ages Newborn +", Keys.ENTER)
    home_page.find_element(By.LINK_TEXT, "Bright Starts Oball Shaker Rattle Toy, Ages Newborn +").click()
    home_page.find_element(By.ID, "add-to-cart-button").click()
    home_page.find_element(By.LINK_TEXT,"Go to Cart").click()
    print('Item added to cart successfully')
    home_page.close()





