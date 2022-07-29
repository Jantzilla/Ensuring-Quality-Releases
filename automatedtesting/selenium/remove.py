from selenium.webdriver.common.by import By
from helper import assertCartCount

def removeItemsFromCart (driver):
    print ('Removing all items from cart...')
    driver.find_element(By.CSS_SELECTOR, "button[id='remove-sauce-labs-backpack']").click()
    assertCartCount(driver, "5")
    print ('Removed backpack from cart.')
    driver.find_element(By.CSS_SELECTOR, "button[id='remove-sauce-labs-bike-light']").click()
    assertCartCount(driver, "4")
    print ('Removed bike light from cart.')
    driver.find_element(By.CSS_SELECTOR, "button[id='remove-sauce-labs-bolt-t-shirt']").click()
    assertCartCount(driver, "3")
    print ('Removed grey t-shirt from cart.')
    driver.find_element(By.CSS_SELECTOR, "button[id='remove-sauce-labs-fleece-jacket']").click()
    assertCartCount(driver, "2")
    print ('Removed jacket from cart.')
    driver.find_element(By.CSS_SELECTOR, "button[id='remove-sauce-labs-onesie']").click()
    assertCartCount(driver, "1")
    print ('Removed onesie from cart.')
    driver.find_element(By.CSS_SELECTOR, "button[id='remove-test.allthethings()-t-shirt-(red)']").click()
    print ('Removed red t-shirt from cart.')

    # Checks that the cart count indicator no longer exists in the webpage.
    assert not len(driver.find_elements(By.CSS_SELECTOR, "span[class='shopping_cart_badge']"))
    
    print ('All items removed from cart successfully! \n')