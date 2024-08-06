from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv
import time
import re

driver = webdriver.Chrome()

driver.get("https://building.cdaid.org/Permit/Search.aspx/")

time.sleep(4)

type_modal = driver.find_element(By.XPATH, '//select[@name="ctl00$ContentPlaceHolder1$cmboType"]')
type_modal.click()

time.sleep(4)

option_select = driver.find_element(By.XPATH, '//option[@value="Re-Roof"]')
option_select.click()

time.sleep(4)

submit_btn = driver.find_element(By.XPATH, '//input[@value="Submit Address Search"]')
submit_btn.click()

time.sleep(4)

headers = driver.find_element(By.XPATH, '//table[@id="ContentPlaceHolder1_grdResults"]//tr[1]')

