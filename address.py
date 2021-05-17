import xml.etree.ElementTree as ET
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import openpyxl

driver_path = "driver/chromedriver"
driver = webdriver.Chrome(executable_path=driver_path)
driver.implicitly_wait(10)
park_list = ["埼玉県　新堀公演"]
address_list = []
for park in park_list:
    driver.get("https://www.google.co.jp/")
    driver.find_element(By.NAME, "q").click()
    kensaku = park + "　住所"
    driver.find_element(By.NAME, "q").send_keys(kensaku + Keys.ENTER)
    """
    try:
        a = driver.find_element(By.CSS_SELECTOR, "div.sXLaOe")
        address_list.append(a.text)
    except:
        break
        """
    try:
        sex=driver.find_element(By.CSS_SELECTOR,"span.LrzXr")
        address_list.append(sex.text)
        """a = driver.find_element(By.CSS_SELECTOR, "div.sXLaOe")
        address_list.append(a.text)"""
    except:
        driver.find_element(By.CSS_SELECTOR, ".uMdZh:nth-child(1) .dbg0pd > span").click()
        #tmp=driver.find_element(By.CSS_SELECTOR,"div.zloOqf PZPZlf")
        sex=driver.find_element(By.CSS_SELECTOR,"span.LrzXr")
        address_list.append(sex.text)
    #s = a.find_element(By.CSS_SELECTOR, "span.GRkHZd w8qArf")
driver.quit()
