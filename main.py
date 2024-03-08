import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service

# Set the path to the Microsoft Edge WebDriver executable
edge_driver_path = r"C:\\msedgedriver.exe"  # Replace with the actual path

# Create a new instance of the Edge driver with the specified executable path
driver = webdriver.Edge(service=Service(edge_driver_path))

# URL to search
search_url = 'https://www.bing.com/'

# List of search terms (place them here)
search_terms = ['example', 'example1', 'example2']

# Time interval between searches in seconds (adjust as needed)
min_delay_search = 5  # minimum delay between searches in seconds
max_delay_search = 15  # maximum delay between searches in seconds

# Time interval between typing each character (adjust as needed)
min_delay_type_char = 0.5  # minimum delay between typing each character in seconds
max_delay_type_char = 1.5  # maximum delay between typing each character in seconds

# Additional delay after typing the complete search term
additional_delay_after_typing = 1.5  # adjust as needed

try:
    while True:
        for term in search_terms:
            # Navigate to the Bing homepage
            driver.get(search_url)

            # Find the search bar element
            search_bar = driver.find_element("name", "q")

            # Create an ActionChains object to simulate typing and clicking
            actions = ActionChains(driver)

            # Simulate typing the search term slowly
            for char in term:
                actions.send_keys(char)
                actions.perform()  # Perform the action after each character
                time.sleep(random.uniform(min_delay_type_char, max_delay_type_char))

            # Additional delay after typing the complete search term
            time.sleep(additional_delay_after_typing)

            # Use send_keys to directly type the complete search term
            search_bar.clear()
            search_bar.send_keys(term)

            actions.send_keys(Keys.RETURN).perform()

            # Introduce a random delay before the next search
            delay_search = random.uniform(min_delay_search, max_delay_search)
            time.sleep(delay_search)

        # Wait for the specified interval before the next round of searches
        time.sleep(random.uniform(min_delay_search, max_delay_search))

except KeyboardInterrupt:
    # Close the browser window if the program is interrupted (e.g., by pressing Ctrl+C)
    driver.quit()
