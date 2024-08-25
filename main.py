# инициализация
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
import os


driver = webdriver.Chrome()
driver.get('https://demoqa.com/automation-practice-form')

first_name_field = driver.find_element(By.XPATH, '//*[@id="firstName"]')
first_name_field.send_keys('Сергей')

last_name_field = driver.find_element(By.XPATH, '//*[@id="lastName"]')
last_name_field.send_keys('Сыроежкин')

email_field = driver.find_element(By.CSS_SELECTOR, '#userEmail')
email_field.send_keys('name@example.com')
sleep(3)

gender_option = driver.find_element(By.XPATH, '//label[@class="custom-control-label" and contains(text(),"Male")]')
gender_option .click()
sleep(3)
mobile_num = driver.find_element(By.CSS_SELECTOR, "#userNumber")
mobile_num.send_keys('8911111111')
sleep(3)


date_field = driver.find_element(By.ID, 'dateOfBirthInput')
date_field.click()

date_field.send_keys(Keys.ENTER)
sleep(3)
subj_element = driver.find_element(By.ID, 'subjectsInput')
#subj_element.send_keys('Math')
#subj_element.send_keys(Keys.ENTER)
#subj_element.send_keys('English')
#subj_element.send_keys(Keys.ENTER)
subj_element.send_keys('History')
subj_element.send_keys(Keys.ENTER)
sleep(3)
pic_upload = driver.find_element(By.CLASS_NAME, 'form-control-file')
pic_upload.send_keys('D:\Work\kotik.jpg')
sleep(3)
SELECT_LOCATOR_ST = ("xpath", "//input[@id='react-select-3-input']")
dropdown_field_st = driver.find_element(*SELECT_LOCATOR_ST).send_keys('Haryana')
dropdown_field_ent1 = driver.find_element(*SELECT_LOCATOR_ST).send_keys(Keys.ENTER)
SELECT_LOCATOR_CT = ("xpath", "//input[@id='react-select-4-input']")
sleep(5)
dropdown_field_ct = driver.find_element(*SELECT_LOCATOR_CT).send_keys('Panipat')
dropdown_field_ent2 = driver.find_element(*SELECT_LOCATOR_CT).send_keys(Keys.ENTER)
sleep(5)
find_button = driver.find_element(By.XPATH, '//*[text()="Submit"]')
find_button.click()
sleep(5)