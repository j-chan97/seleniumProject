from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(xecutable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://orteil.dashnet.org/cookieclicker/")

product_prefix = "product"
product_price_prefix = "productPrice"

WebDriverWait(driver, 5).until (

    EC.presence_of_element_located((By.ID, "langSelect-EN"))
)
language = driver.find_element(By.ID, "langSelect-EN")
language.click()

time.sleep(5)

WebDriverWait(driver, 5).until (
    EC.presence_of_element_located((By.ID, "bigCookie"))
)

cookie = driver.find_element(By.ID, "bigCookie")

while True:
    cookie.click()
    cookie_no = driver.find_element(By.ID, "cookies").text.split(" ")[0]
    cookie_no = int(cookie_no.replace(",", ""))
    # print(cookie_no)

    for i in range(5):
        product_price = driver.find_element(By.ID, product_price_prefix + str(i)).text
        # print(product_price)
        if product_price == "":
            continue

        product_price = int(product_price.replace(",", ""))

        if cookie_no >= product_price:
            product_name = driver.find_element(By.ID, product_prefix + str(i))
            product_name.click()
            break

    # cursor = driver.find_element(By.ID, "product0")
    # cursor_price = int(driver.find_element(By.ID, "productPrice0").text)
    #
    # if cookie_no >= cursor_price:
    #     cursor.click()



