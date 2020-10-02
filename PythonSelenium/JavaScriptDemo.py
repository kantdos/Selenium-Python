# JavaScript DOM can access any elements on web page just like how selenium does
# Selenium have a method to execute JavaScript code in it
from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\\Selenium\\Driver\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element_by_name("name").send_keys("Hello")
print(driver.find_element_by_name("name").get_attribute("value"))
print(driver.execute_script('return document.getElementsByName("name")[0].value'))  # JavaScript
shopButton = driver.find_element_by_css_selector("a[href*='shop']")
driver.execute_script('arguments[0].click();', shopButton) # JavaScript

driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

# driver.close()
