# login.py
import time
import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By

def linkedin_login(driver, email, password):
    driver.get("https://www.linkedin.com/login")
    time.sleep(2)

    # Enter Email
    email_field = driver.find_element(By.ID, "username")
    email_field.send_keys(email)

    # Enter Password
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys(password)

    # Click Login
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # Wait for manual login or MFA approval
    print("Please manually complete the login and navigate to the LinkedIn homepage.")
    input("Press Enter once you're on the LinkedIn homepage...")

    # Save cookies to a file
    pickle.dump(driver.get_cookies(), open("linkedin_cookies.pkl", "wb"))
    print("Session cookies saved successfully!")
