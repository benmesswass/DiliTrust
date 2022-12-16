import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://gov.dilitrust.com/")
time.sleep(5)

mailField = driver.find_element(By.ID, "login-name-input")
mailField.send_keys("wassimbenmessaoud@gmail.com")
time.sleep(5)

loginButton = driver.find_element(By.ID, "login-button")
loginButton.click()
time.sleep(5)

passwordField = driver.find_element(By.ID, "login-password-input")
passwordField.send_keys("wassimbenmessaoud")
time.sleep(5)

loginButton.click()
time.sleep(5)

errorMessage = driver.find_element(By.ID, "login-form-error-0-message").text

assert (errorMessage == "Désolé, e-mail ou mot de passe non reconnu. Avez-vous oublié votre mot de passe ?")

driver.close()
