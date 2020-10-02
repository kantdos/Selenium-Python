import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

list1 = []
list2 = []
driver = webdriver.Chrome(executable_path="D://Selenium//Driver//chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(6)  # Global wait (Implicit wait)
driver.maximize_window()
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")

time.sleep(3)
products = driver.find_elements_by_xpath("//div[@class='products']/div")
count = len(products)
assert count == 3

buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")  # //div[@class='product-action']/button/parent::div/parent::div/h4
for button in buttons:
    list1.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)
    button.click()
print(list1)

driver.find_element_by_css_selector("img[alt='Cart']").click()
time.sleep(5)
driver.find_element_by_xpath("//div[@class='action-block']/button").click()
time.sleep(5)
cartItems = driver.find_elements_by_css_selector("p.product-name")
for cartItem in cartItems:
    print(cartItem.text)
    list2.append(cartItem.text)
print(list2)

assert list1 == list2

wait = WebDriverWait(driver, 7)  # Explicit wait
wait.until(expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR, "input[class='promoCode']")))

originalAmount = driver.find_element_by_css_selector(".discountAmt")
print(originalAmount.text)
driver.find_element_by_css_selector("input[class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()
wait.until(expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR, ".promoInfo")))
conf = driver.find_element_by_css_selector(".promoInfo").text
print(conf)

finalAmount = driver.find_element_by_css_selector(".discountAmt")
print(finalAmount.text)
# assert float(finalAmount.text) < int(originalAmount.text)

amounts = driver.find_elements_by_xpath("//tr/td[5]/p")
sum1 = 0
for amount in amounts:
    sum1 = sum1 + int(amount.text)
print(sum1)
sumAmount = driver.find_element_by_css_selector(".totAmt")
print(sumAmount.text)
assert sum1 == int(sumAmount.text)