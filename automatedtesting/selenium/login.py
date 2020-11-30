# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions

url = "https://www.saucedemo.com/"
inventory_url = "https://www.saucedemo.com/inventory.html"

# Start the browser and login with standard_user
def login (user, password):
    print ("Logging in with" ,user, "with password", password)	
    driver.find_element_by_id('user-name').send_keys(user)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_id('login-button').click()
    assert inventory_url in driver.current_url
    print ('Test login success')
	
def add_to_cart(item_title, button):
    print("Adding", item_title,  "to cart")
    button.click()

def remove_from_cart(item_title, button):
    print("Removing",  item_title, "from cart")
    button.click()

if __name__ == "__main__":
    print('#'*79)
    print('Staring UI Test')
    print('#'*79)
    print ('Starting the browser...')
    options = ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    print ('Browser started successfully. Navigating to the demo page to login.')
    driver.get(url)
    
    login('standard_user', 'secret_sauce')

    inventory_items = driver.find_elements(By.CLASS_NAME, "inventory_item")

    # Add all items
    for item in inventory_items:
        title = item.find_element(By.CLASS_NAME, "inventory_item_name").text
        button = item.find_element(
            By.CSS_SELECTOR, "button[class='btn_primary btn_inventory']"
        )
        add_to_cart(title, button)
    
    # Go to basket
    cart_button = driver.find_element(
        By.CSS_SELECTOR, "a[class='shopping_cart_link fa-layers fa-fw']"
    )
    cart_button.click()
    
    # Get items
    basket = driver.find_elements(By.CLASS_NAME, "cart_item")
    
    # Remove items
    for item in basket:
        title = item.find_element(By.CLASS_NAME, "inventory_item_name").text
        button = item.find_element(
            By.CSS_SELECTOR, "button[class='btn_secondary cart_button']"
        )
        remove_from_cart(title, button)
    
    print('#'*33, 'end of test', '#'*33)
    