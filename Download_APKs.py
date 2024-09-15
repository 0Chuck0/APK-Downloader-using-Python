from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

def create_driver_instance():
    # Path to the Brave browser executable
    brave_path = "C:/Users/sshah/AppData/Local/BraveSoftware/Brave-Browser/Application/brave.exe"  # Update this path as necessary
    
    # Set Chrome options to use the Brave browser
    options = Options()
    options.binary_location = brave_path
    options.add_argument("--start-maximized")  # Start browser maximized
    prefs = {
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    }
    options.add_experimental_option("prefs", prefs)  # Set download preferences
    options.add_experimental_option("detach", True)
    options.page_load_strategy = 'eager'
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)  # Create the WebDriver instance
    return driver

def download_apk():
    # URL of the page to scrape
    url = "https://apkpure.net/social"
    driver = create_driver_instance()
    driver.get(url)  # Navigate to the page

    try:
        print("Start")
        # Wait until the element with the specified attribute is present
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@data-dt-module-name="downloads"]'))
        )
        print("Button found")
        download_btn = driver.find_element(By.XPATH, '//*[@data-dt-module-name="downloads"]')
        
        # Scroll to the download button and click it
        driver.execute_script("""arguments[0].scrollIntoView(true);
                               arguments[0].click();""", download_btn)
        print("Download Button Clicked")
        time.sleep(1)  # Wait for 1 second
        
        # Wait until the download links are present
        WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "apk-grid-download"))
        )
        print("Fetch")
        
        # Parse the page source with BeautifulSoup
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        visible_divs = soup.find_all('div', class_='tab-item', style=lambda value: value and 'display: block' in value)        
        if visible_divs:
            visible_div = visible_divs[0]  # Assuming only one div is visible at a time
            download_links = visible_div.find_all('a', class_="apk-grid-download", limit=5)
        else:
            download_links = []
        
        # Iterate over the download links
        for idx, link in enumerate(download_links):
            new_url = link.get("href")  # Get the href attribute of the link
            new_url += "ing"  # Append "ing" to the URL (if necessary)
            print(f"Downloading app {idx+1}")
            driver.get(new_url)  # Navigate to the new URL
            time.sleep(1)  # Wait for 1 second
            # driver.back()  # Go back to the previous page

        print("5 Apps Download Completed")

    except Exception as e:
        print(f"An error occurred: {e}")

    # finally:
        # Close the WebDriver instance
        # driver.quit()

# Run the script
if __name__ == "__main__":
    download_apk()
