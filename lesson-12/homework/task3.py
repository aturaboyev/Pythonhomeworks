import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Setup Selenium WebDriver
options = Options()
options.add_argument("--headless")  # Run in headless mode
service = Service("chromedriver")  # Path to chromedriver

driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.demoblaze.com/")

# Navigate to Laptops section
driver.find_element(By.LINK_TEXT, "Laptops").click()
time.sleep(2)

laptop_data = []

while True:
    # Find all laptop entries
    items = driver.find_elements(By.CLASS_NAME, "card")

    for item in items:
        name = item.find_element(By.CLASS_NAME, "card-title").text
        price = item.find_element(By.CLASS_NAME, "price-container").text.split()[0]  # Extract price
        description = item.find_element(By.CLASS_NAME, "card-text").text

        laptop_data.append({"name": name, "price": price, "description": description})

    # Try to click the "Next" button
    try:
        next_button = driver.find_element(By.LINK_TEXT, "Next")
        next_button.click()
        time.sleep(2)
    except:
        break  # No more pages

# Save data to JSON
with open("laptops.json", "w", encoding="utf-8") as file:
    json.dump(laptop_data, file, indent=4)

driver.quit()
print("Laptop data saved to laptops.json")
