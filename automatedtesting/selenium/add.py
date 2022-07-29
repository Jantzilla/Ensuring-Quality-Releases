from selenium.webdriver.common.by import By
from helper import assertCartCount

def addItemsToCart (driver):
    print ('Adding all items to cart...')
    driver.find_element(By.CSS_SELECTOR, "button[id='add-to-cart-sauce-labs-backpack']").click()
    assertCartCount(driver, "1")
    print ('Added backpack to cart.')
    driver.find_element(By.CSS_SELECTOR, "button[id='add-to-cart-sauce-labs-bike-light']").click()
    assertCartCount(driver, "2")
    print ('Added bike light to cart.')
    driver.find_element(By.CSS_SELECTOR, "button[id='add-to-cart-sauce-labs-bolt-t-shirt']").click()
    assertCartCount(driver, "3")
    print ('Added grey t-shirt to cart.')
    driver.find_element(By.CSS_SELECTOR, "button[id='add-to-cart-sauce-labs-fleece-jacket']").click()
    assertCartCount(driver, "4")
    print ('Added jacket to cart.')
    driver.find_element(By.CSS_SELECTOR, "button[id='add-to-cart-sauce-labs-onesie']").click()
    assertCartCount(driver, "5")
    print ('Added onesie to cart.')
    driver.find_element(By.CSS_SELECTOR, "button[id='add-to-cart-test.allthethings()-t-shirt-(red)']").click()
    assertCartCount(driver, "6")
    print ('Added red t-shirt to cart.')

    print ('All items added to cart successfully! \n')