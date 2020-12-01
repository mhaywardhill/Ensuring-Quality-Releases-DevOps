import logging 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time

timestamp = time.strftime('%b-%d-%Y_%H%M')
output_file = "/var/log/selenium/uitest_"+timestamp+".log"

#Create and configure logger 
logging.basicConfig(filename=output_file, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filemode='w') 
#Creating an object 
logger=logging.getLogger() 
  
#Setting the threshold of logger to DEBUG 
logger.setLevel(logging.DEBUG) 

# Start the browser and login with standard_user
def login (driver,user, password):
    logger.info("Logging in with '%s' with password '%s'", user, password)	
    driver.find_element_by_id('user-name').send_keys(user)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_id('login-button').click()
    logger.info ("Test login success")

def add_to_cart(item_title, button):
    logger.info("Adding '%s' to cart",item_title)
    button.click()

def remove_from_cart(item_title, button):
    logger.info("Removing '%s' from cart", item_title)
    button.click()

def main():
    logger.info("Starting the UI test")
    logger.info("Starting the browser")
    options = ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    logger.info("Browser started successfully. Navigating to the demo page to login")
    driver.get("https://www.saucedemo.com/")

    login(driver, 'standard_user', 'secret_sauce')

    # Get all inventory items
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
    
    # Get items in basket
    basket = driver.find_elements(By.CLASS_NAME, "cart_item")

    # Remove items
    for item in basket:
        title = item.find_element(By.CLASS_NAME, "inventory_item_name").text
        button = item.find_element(
            By.CSS_SELECTOR, "button[class='btn_secondary cart_button']"
        )
        remove_from_cart(title, button)	

    logger.info("Finished the UI test")

if __name__ == "__main__":
    main()