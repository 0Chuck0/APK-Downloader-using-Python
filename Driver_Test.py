from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time


url = "https://www.google.com"
url2 = "https://erp.daiict.ac.in"
options = Options()
options.add_argument("--start-maximized")
prefs = {
    "detach" : True,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
}
options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.get(url)
time.sleep(2)
driver.get(url2)
time.sleep(2)
driver.back()
time.sleep(10)