from selenium import webdriver
from selenium.webdriver.common.by import By

#initialise driver
driver = webdriver.Chrome()

#access webpage
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

#wait
driver.implicitly_wait(1)

#find elements
text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

#input value into textbox and click submit button
text_box.send_keys("Selenium")
submit_button.click()

#Verify a message
message = driver.find_element(by=By.ID, value="message")
text = message.text

#get title and print values
title = driver.title
print(title)
print(text)

#end session
driver.quit()
