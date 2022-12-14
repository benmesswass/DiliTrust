import time

from selenium import webdriver
from selenium.webdriver.common.by import By

#driver = webdriver.Firefox("/Users/wassimzenity/Downloads")
driver = webdriver.Chrome("/Users/wassimzenity/Downloads")

driver.get("https://gov.dilitrust.com/")
time.sleep(2)
elem = driver.find_element(By.TAG_NAME, "input")
elem.send_keys("wassim")
driver.close()
