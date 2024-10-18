from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv
import time
import re

username = 'danielrobl3s_SqwcC'
password = '_wBObaboyamama12'
proxy_url = "'https://customer-danielrobl3s_SqwcC:_wBObaboyamama12@pr.oxylabs.io:7777'"

chrome_options = Options()
chrome_options.add_argument('--proxy-server='+f'{proxy_url}')
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.realtor.com/propertyrecord-search/Coeur-d'Alene_ID")

time.sleep(10)