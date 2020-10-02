from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="D:\\Selenium\\Driver\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element_by_name("name").send_keys("Ravi Kant")
# driver.find_element_by_css_selector("input[name='name']").send_keys("Ravi")
driver.find_element_by_css_selector("input[name='email']").send_keys("kant.dos@gmail.com")
# driver.find_element_by_name("email").send_keys("kant.dos@gmail.com")
driver.find_element_by_id("exampleInputPassword1").send_keys("Asdf123")
driver.find_element_by_id("exampleCheck1").click()
# select class provide the methods to handle the options in dropdown
dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
# dropdown.select_by_value("Female")
driver.find_element_by_xpath("//input[@type='submit']").click()
driver.get_screenshot_as_file("D:\\ss.png")
# print(driver.find_element_by_class_name("alert-success").text)
message = driver.find_element_by_css_selector("[class*='alert-success']").text # /*[contains(@class,'alert-success')] - xpath
assert "Success" in message
driver.close()