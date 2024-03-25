from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get("https://play2048.co/")

title = driver.title

# Function to get the current state of the game grid
def get_game_state(driver):
    game_state = []
    tiles = driver.find_elements_by_class_name("tile")
    for tile in tiles:
        tile_class = tile.get_attribute("class").split()
        tile_value = int(tile_class[1][len("tile-"):])
        tile_position = tile.get_attribute("class").split()[2:]
        tile_position = [int(coord[coord.index("-") + 1 :]) for coord in tile_position]
        game_state.append((tile_position, tile_value))
    return game_state

# Function to calculate the total score after making a move
def calculate_score(game_state):
    total_score = 0
    for position, value in game_state:
        total_score += value
    return total_score

# Function to make a move based on the strategy
def make_move(driver, direction):
    driver.find_element_by_tag_name("body").send_keys(direction)

# Function to find the best move
def find_best_move(driver):
    directions = [Keys.ARROW_LEFT, Keys.ARROW_RIGHT, Keys.ARROW_DOWN]
    max_score = float('-inf')
    best_move = None
    for direction in directions:
        temp_driver = driver
        make_move(temp_driver, direction)
        time.sleep(2.0)  # Allow time for the animation to complete
        current_score = calculate_score(get_game_state(temp_driver))
        if current_score > max_score:
            max_score = current_score
            best_move = direction
    return best_move

# Main function to play the game
def play_game():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://play2048.co/")
    try:
        while True:
            best_move = find_best_move(driver)
            if best_move:
                make_move(driver, best_move)
                time.sleep(2.0)
            else:
                break  # No valid move found
    finally:
        driver.quit()

if __name__ == "__main__":
    play_game()