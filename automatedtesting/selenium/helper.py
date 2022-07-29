from selenium.webdriver.common.by import By

def assertCartCount (driver, expectedCount):
    # Checks that the cart count matches the currently expected count.
    cartCount = driver.find_element(By.CSS_SELECTOR, "span[class='shopping_cart_badge']").text
    assert expectedCount == cartCount