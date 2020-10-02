from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="D:\\Selenium\\Driver\\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element_by_css_selector("a[href*='shop']").click()
products = driver.find_elements_by_css_selector("div.card")
print(products)
for product in products:
    productName = product.find_element_by_css_selector("div h4 a").text  # div.card div h4 a
    if productName == "Blackberry":
        product.find_element_by_css_selector("div button").click()

driver.find_element_by_css_selector(".btn-primary").click()
driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
driver.find_element_by_id("country").send_keys("Ind")
wait = WebDriverWait(driver, 7)
wait.until(expected_conditions.presence_of_all_elements_located((By.LINK_TEXT,"India")))
driver.find_element_by_link_text("India").click()
driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
driver.find_element_by_css_selector(".btn-success").click()
message = driver.find_element_by_class_name("alert-success").text
print(message)
assert "Success" in message
driver.get_screenshot_as_file("D://ss.png")


# driver.close()
