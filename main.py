from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument('detach')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get('http://www.python.org')
