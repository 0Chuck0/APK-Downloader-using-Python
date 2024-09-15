import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup




def get_app_links(options):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
    driver.get("https://play.google.com/store/apps")
    try:
        # Wait for the elements with the class 'Si6A0c itIJzb' to be present
        WebDriverWait(driver, 50).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a.Si6A0c.ZD8Cqc'))
        )

        # Get the page source after the elements are loaded
        page_source = driver.page_source

        # Parse the page source with BeautifulSoup
        soup = BeautifulSoup(page_source, 'html.parser')

        # Extract app links
        prefix = "https://play.google.com"
        all_list = soup.select("a.Si6A0c.ZD8Cqc",limit=50)
        links = [prefix + link.get("href") for link in all_list]
        return links
    except:
        print("Error occured while fetching the links")
        return []
    finally:
        # Close the WebDriver
        driver.quit()

# Write all the links generated in another text file
def write_links_to_file(links, file_path):
    if not links:
        print("No Links Were Fetched")
    else:
        with open(file_path, 'w') as file:
            for link in links:
                file.write(f"{link}\n")
        print(f"App links have been written to {file_path}")

options = Options()
options.add_experimental_option("detach",True)
# Get the app links
# app_links = get_app_links(options)

# # Write the app links to a file
# output_file_path = 'app_links.txt'
# write_links_to_file(app_links, output_file_path)



#Create the new driver instance for downloading the links 

def download_apk(url):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
    driver.get("https://apps.evozi.com/apk-downloader/")
    try:
        # Wait for the elements with the class 'Si6A0c itIJzb' to be present
        WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.ID, 'ahVlGflRRtpdkl'))
        )
        input_box = driver.get_element({By.ID,'ahVlGflRRtpdkl'})
        input_box.send_keys(url)
        # Get the page source after the elements are loaded
        # page_source = driver.page_source

        # # Parse the page source with BeautifulSoup
        # soup = BeautifulSoup(page_source, 'html.parser')

        # # Extract app links
        # prefix = "https://play.google.com"
        # all_list = soup.select("a.Si6A0c.ZD8Cqc",limit=50)
        # links = [prefix + link.get("href") for link in all_list]
        # return links
    except:
        print("Error occured while pasting the link")
        return []
    finally:
        # Close the WebDriver
        driver.quit()

download_apk("https://play.google.com/store/apps/details?id=com.whatsapp")
