from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
import csv
import time
import re

driver = uc.Chrome()

def get_title():
    title = driver.find_element(By.XPATH, '//h2[@class="base__StyledType-rui__sc-108xfm0-0 jzOnZ"]').text

    return title

def get_links():
    time.sleep(2)

    links = len(driver.find_elements(By.XPATH, '//ul[@class="sc-4316f608-0 dtcbmP"]//a'))

    with open(f'{file_name}.txt', 'w', encoding='utf-8') as file:
        for link in range(1, links+1):
            time.sleep(2)
            a = driver.find_element(By.XPATH, '//*[@id="street"]/ul/li'+f'[{link}]'+'//a')

            a.click()

            time.sleep(2)

            in_links = len(driver.find_elements(By.XPATH, '//ul[@class="list-column_home_value"]//li/a'))

            for i in range(1, in_links+1):
                time.sleep(2)
                a = driver.find_element(By.XPATH, '//*[@id="home-values"]/ul/div'+f'[{i}]'+'/div[1]/li/a')
                a.click()
                time.sleep(2)

                data = driver.find_element(By.XPATH, '//div[@class="Box__StyledBox-rui__sc-16jloov-0 eQUfKK Flex__StyledFlex-rui__sc-19d2399-0 fMFHoW styles__MainFactsColumn-sc-1xvl3o5-11 JtMq"]').text
                file.write(data)

                time.sleep(2)

                back_btn = driver.find_element(By.XPATH, '//button[@data-testid="back-button"]')
                back_btn.click()

                time.sleep(2)


driver.get("https://www.realtor.com/propertyrecord-search/Coeur-d'Alene_ID")
file_name = input('Name your csv file: ')

time.sleep(2)

title = get_title()

get_links()

