from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

CHROME_DRIVER_PATH = "C:\Program Files\Google\Chrome\Application\chrome.exe"

options = Options()
options.add_argument("--headless")
service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("https://www.google.com")
    print("ChromeDriver is working!")
finally:
    driver.quit()

