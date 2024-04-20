from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Set the URL you want to scrape
url = "https://example.com"

# Open the URL in the Chrome browser
driver.get(url)

# Wait for the page to load completely
wait = WebDriverWait(driver, 10)

# Example: Wait until the element with ID "element_id" is visible
element_id = "element_id"
element = wait.until(EC.visibility_of_element_located((By.ID, element_id)))

# Once the element is visible, you can perform actions on it
print("Element with ID {} is visible".format(element_id))

# Example: Get the text of the visible element
element_text = element.text
print("Text of the element: {}".format(element_text))

# Close the browser window
driver.quit()
