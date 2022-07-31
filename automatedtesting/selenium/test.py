# #!/usr/bin/env python
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from login import login
from add import addItemsToCart
from remove import removeItemsFromCart

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

# --uncomment when running in Azure DevOps.
options = ChromeOptions()
options.add_argument('--headless')
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.add_argument("--window-size=1920,1080")
options.add_argument("--remote-debugging-port=9222")

# Ubuntu 18 VM
driver = webdriver.Chrome(options=options)

# Ubuntu 20 VM
# driver = webdriver.Chrome(options=options, executable_path='/snap/bin/chromium.chromedriver')
# driver = webdriver.Chrome()

# Start the browser and login with standard_user
def runTest ():
    logging.info('')
    print ('Starting the browser...')
    print ('Browser started successfully.')
    print ('Navigating to the demo page to login \n')

    driver.get('https://www.saucedemo.com/')

    login(driver, 'standard_user', 'secret_sauce')
    addItemsToCart(driver)
    removeItemsFromCart(driver)

runTest()