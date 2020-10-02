import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
driver = webdriver.Chrome(options=options, executable_path="D://Selenium//Driver//chromedriver.exe")

#iFrame, frameset, frame
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.maximize_window()
# menu = driver.find_element_by_id("mousehover")
# action.move_to_element(menu).perform()
# action.move_to_element(driver.find_element_by_link_text("Reload")).click().perform()

driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
action = ActionChains(driver)
time.sleep(3)
action.context_click(driver.find_element_by_id("double-click")).perform() # Double click
action.double_click(driver.find_element_by_id("double-click")).perform()
alert = driver.switch_to.alert
assert "You double clicked me!!!, You got to be kidding me" == alert.text
alert.accept()
driver.quit()