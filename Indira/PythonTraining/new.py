import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



# Set up the browser
def test_website():
        test_browser = webdriver.Firefox()
        time.sleep(10)


# Navigate to the Domino's website
       test_browser.get("https://www.dominos.com/en/")

# Click on the Sign In button
    sign_in_button = browser.find_element_by_link_text("Sign in & earn rewards")
    sign_in_button.click()


# Fill in the email and password fields and click the Sign In button
    email_field = browser.find_element_by_id("Email")
    email_field.send_keys("your_email@example.com")

    password_field = browser.find_element_by_id("Password")
    password_field.send_keys("your_password")

sign_in_modal.find_element_by_id("sign-in-button").click()



# Click the Join button
rewards_modal.find_element_by_link_text("Join").click()

# Fill in the required fields on the registration form
first_name_field = browser.find_element_by_id("first_name")
first_name_field.send_keys("Your First Name")

last_name_field = browser.find_element_by_id("last_name")
last_name_field.send_keys("Your Last Name")

email_field = browser.find_element_by_id("email")
email_field.send_keys("your_email@example.com")

confirm_email_field = browser.find_element_by_id("confirm_email")
confirm_email_field.send_keys("your_email@example.com")

password_field = browser.find_element_by_id("password")
password_field.send_keys("your_password")

phone_field = browser.find_element_by_id("phone")
phone_field.send_keys("1234567890")

address_field = browser.find_element_by_id("street")
address_field.send_keys("123 Main St")

city_field = browser.find_element_by_id("city")
city_field.send_keys("Your City")

state_field = browser.find_element_by_id("state")
state_field.send_keys("Your State")

zip_field = browser.find_element_by_id("zip")
zip_field.send_keys("12345")

# Submit the registration form
rewards_modal.find_element_by_id("register-button").click()

# Close the browser
browser.quit()