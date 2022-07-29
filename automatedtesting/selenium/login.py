# #!/usr/bin/env python
from selenium.webdriver.common.by import By

def login (driver, user, password):
    print (f'Logging in as {user}...')
    driver.find_element(By.CSS_SELECTOR, "input[id='user-name']").send_keys(user)
    driver.find_element(By.CSS_SELECTOR, "input[id='password']").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "input[id='login-button']").click()

    pageTitle = driver.find_element(By.CSS_SELECTOR, "span[class='title']").text
    assert pageTitle == "PRODUCTS"

    print (f'Login as {user} successful! \n')