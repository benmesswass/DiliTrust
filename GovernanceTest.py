import time

from selenium import webdriver
from selenium.webdriver.common.by import By

#driver = webdriver.Firefox("/Users/wassimzenity/Downloads")
driver = webdriver.Chrome()

driver.get("https://gov.dilitrust.com/")
time.sleep(5)

mailField = driver.find_element(By.ID, "login-name-input")
mailField.send_keys("wassimbenmessaoud@gmail.com")

loginButton = driver.find_element(By.ID, "login-button-button")
loginButton.click()

passwordField = driver.find_element(By.ID, "login-password-input")
passwordField.send_keys("wassimbenmessaoud")

loginButton.click()

errorMessage = driver.find_element(By.ID, "login-form-error-0-message")
assert (errorMessage.getAttribute("data-v-4d394ef5") == "Désolé, e-mail ou mot de passe non reconnu. ")

driver.close()
