import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\\Selenium\\Driver\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()
driver.find_element_by_id("autosuggest").send_keys("ind")
time.sleep(2)
countries = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")
print(len(countries))

for country in countries:
    if country.text == "India":
        country.click()
        break
assert driver.find_element_by_id("autosuggest").get_attribute('value') == "India"

driver.find_element_by_id("ctl00_mainContent_ddl_originStation1_CTXT").send_keys("de")
time.sleep(2)
driver.find_element_by_xpath("//a[contains(text(),'Delhi')]").click()
driver.find_element_by_id("ctl00_mainContent_ddl_destinationStation1_CTXT").send_keys("Kol")
time.sleep(2)
driver.find_element_by_xpath("//a[contains(text(),'Kolk')]").click()


# driver.close()