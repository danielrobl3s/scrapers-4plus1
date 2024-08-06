from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import nltk
from nltk.tokenize import word_tokenize
import csv
import time
import re


nltk.download('punkt')

#Clicking modal and choosing type of building on Cour D'Alene, Idaho, U.S.

def click_modal():
    type_modal = driver.find_element(By.XPATH, '//select[@name="ctl00$ContentPlaceHolder1$cmboType"]')
    type_modal.click()

    time.sleep(4)

    option_select = driver.find_element(By.XPATH, '//option[@value="Re-Roof"]')
    option_select.click()

    time.sleep(4)

    submit_btn = driver.find_element(By.XPATH, '//input[@value="Submit Address Search"]')
    submit_btn.click()

    time.sleep(10)


driver = webdriver.Chrome()

driver.get("https://building.cdaid.org/Permit/Search.aspx/")
file_name = input('Name your csv file: ')
name = file_name + '.csv'

time.sleep(4)

click_modal()

links = len(driver.find_elements(By.XPATH, '//table[@id="ContentPlaceHolder1_grdResults"]//a'))

for link in range(2, links+1):

    time.sleep(5)

    a = driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_grdResults"]/tbody/tr'+f'[{link}]'+'/td/a')

    a.click()

    data = driver.find_elements(By.XPATH, '//div[@id="TabStrip-1"]/div')

    for element in data:
        print(element.text)

    back = driver.find_element(By.XPATH, '//div[@style="text-align: center;"]/a')
    back.click()

    click_modal()