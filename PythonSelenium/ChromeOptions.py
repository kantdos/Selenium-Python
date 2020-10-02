from selenium import webdriver

chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")


driver = webdriver.Chrome(executable_path="D:\\Selenium\\Driver\\chromedriver.exe",options=chrome_options)
driver.get("https://rahulshettyacademy.com/angularpractice/")

''' Use Navigation Timing  API to calculate the timings that matter the most '''

navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
responseStart = driver.execute_script("return window.performance.timing.responseStart")
domComplete = driver.execute_script("return window.performance.timing.domComplete")

''' Calculate the performance'''
backendPerformance_calc = responseStart - navigationStart
frontendPerformance_calc = domComplete - responseStart

print("Back End: %s" % backendPerformance_calc)
print("Front End: %s" % frontendPerformance_calc)

# driver.maximize_window()
print(driver.title)
