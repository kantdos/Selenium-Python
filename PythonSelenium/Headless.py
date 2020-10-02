from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
driver = webdriver.Chrome(options=options, executable_path="D://Selenium//Driver//chromedriver.exe")
driver.get("http://google.com/")
print ("Headless Chrome Initialized")
driver.quit()