from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

# Fill in message prompt and click show message
messageField = driver.find_element_by_xpath('//*[@id="user-message"]')
messageField.send_keys('Hello World!')
showMessageButton = driver.find_element_by_xpath('//*[@id="get-input"]/button')
showMessageButton.click()

# Fill in addition fields and click Get Total
additionField1 = driver.find_element_by_xpath('//*[@id="sum1"]')
additionField1.send_keys('5')
additionField1 = driver.find_element_by_xpath('//*[@id="sum2"]')
additionField1.send_keys('5')
getTotalButton = driver.find_element_by_xpath('//*[@id="gettotal"]/button')
getTotalButton.click()