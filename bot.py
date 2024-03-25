from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Launch the browser and open the game URL
webdriver_path = r'C:\Users\Vid\chromedriver.exe'  # Use raw string (r'') to avoid escape characters
browser = webdriver.Chrome(executable_path=webdriver_path)
browser.get("https://play2048.co/")

# Function to perform a move
def perform_move(move):
    html_elem = browser.find_element_by_tag_name('html')
    html_elem.send_keys(move)

# Example usage:
# Wait for the game to load
time.sleep(2)

# Perform moves
perform_move(Keys.ARROW_UP)
perform_move(Keys.ARROW_DOWN)
perform_move(Keys.ARROW_LEFT)
perform_move(Keys.ARROW_RIGHT)

# Close the browser
browser.quit()
