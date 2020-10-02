from selenium import webdriver

# browser exposes an executable file
# through selenium test we need to invoke the executable file which will then invoke actual browser
driver = webdriver.Chrome(executable_path="D:\\Selenium\\Driver\\chromedriver.exe")
# driver = webdriver.Firefox(executable_path="D:\\Selenium\\Driver\\geckodriver.exe")
driver.get("https://rahulshettyacademy.com/#/index")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
print(driver.title)
print(driver.current_url)
driver.minimize_window()
driver.back()
driver.refresh()
driver.close()
