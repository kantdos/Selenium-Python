from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

# options = Options()
# options.headless = True
driver = webdriver.Chrome(executable_path="D://Selenium//Driver//chromedriver.exe") # options=options,
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

assert driver.find_element_by_id("displayed-text").is_displayed()
driver.find_element_by_id("hide-textbox").click()
assert not driver.find_element_by_id("displayed-text").is_displayed()
driver.close()
