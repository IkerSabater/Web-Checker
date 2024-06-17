from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import subprocess

driverURL = '/path/to/driver'
navbar_id = 'navbar_id'
url = "https://example.com"
appName = 'Web App'

def send_ubuntu_notification(title, message):
    subprocess.run(['notify-send', title, message])

def check_navbar_presence(url, navbar_id):
    try:
        # Set up Chrome options for headless mode
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")  # Applicable only if you have GPU installed
        chrome_options.add_argument("--window-size=1920,1080")  # Optional, can adjust as needed

        # Set up the WebDriver with the correct path to the ChromeDriver executable
        service = Service(driverURL)  # Specify the correct path
        driver = webdriver.Chrome(service=service, options=chrome_options)

        # Navigate to the web page
        driver.get(url)
        time.sleep(5)  # Wait for the page to load

        # Check if the navbar with the specified ID is present
        try:
            navbar = driver.find_element(By.ID, navbar_id)
            if navbar:
                print(f"App is runing")
                return True
        except Exception as e:
            print(f"App is not runing")
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    finally:
        driver.quit()

if __name__ == "__main__":
    check_interval = 60  # Check every 60 seconds
    previous_state = None

    while True:
        current_state = check_navbar_presence(url, navbar_id)
        if current_state != previous_state:
            if current_state:
                send_ubuntu_notification(appName+" Active", f"The web app at {url} is running.")
            else:
                send_ubuntu_notification(appName+" inactive", f"The web app at {url} is not running.")
            previous_state = current_state
        time.sleep(check_interval)
