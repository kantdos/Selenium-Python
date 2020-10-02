import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\\Selenium\\Driver\\chromedriver.exe")
driver.get("https://www.makemytrip.com/")
driver.maximize_window()
time.sleep(3)
driver.find_element_by_id("fromCity").click()
driver.find_element_by_css_selector("#fromCity").send_keys("Pun")
time.sleep(3)
cities = driver.find_elements_by_css_selector("p[class='code makeRelative']")
print(len(cities))
len(cities)
for city in cities:
    if city.text == "Pune":
        city.click()
        break