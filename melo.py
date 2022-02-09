from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import threading
from threading import Thread
import easyimap as e
import re
import pyperclip
from selenium.webdriver.chrome.options import Options
import requests

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-web-security")
chrome_options.add_argument("--disable-translate")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--allow-running-insecure-content")
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options,executable_path='C:\Python\chromedriver.exe')


# url = 'https://dropmail.me/download/mail/gql:anonym-web-test-IDacHoa:1013d1db-80b9-4849-8ca6-e800fdcfc8df/vga92qcrg6c1cvapo4leh9trp724re86'
# def download_file(url):
#     local_filename = url.split('/')[-1]
#     # NOTE the stream=True parameter below
#     with requests.get(url, stream=True) as r:
#         r.raise_for_status()
#         with open(local_filename, 'wb') as f:
#             for chunk in r.iter_content(chunk_size=8192): 
#                 # If you have chunk encoded response uncomment if
#                 # and set chunk_size parameter to None.
#                 #if chunk: 
#                 f.write(chunk)
#     return local_filename
# print(download_file(url))
# input()


while True:
    a = requests.get('https://dropmail.me/api/graphql/web-test-IDacHoa?query=mutation%20%7BintroduceSession%20%7Bid%2C%20expiresAt%2C%20addresses%20%7Baddress%7D%7D%7D').text.split(',')
    #getID
    b = a[0].split('"')
    id = b[7]
    #Get date expire
    d = a[1].split('"')
    date_expire = d[3]
    #Get address
    e = a[2].split('"')
    address = e[5]
    print(address)
    driver.get('https://www.melos.studio/registration?inviteCode=026DBCD4')
    while True:
        try:
            driver.find_element_by_id('nest-messages_email').send_keys(address)
            driver.find_element_by_id('nest-messages_password').send_keys('iloveyoume')
            driver.find_element_by_xpath(r'//*[@id="ant"]/div[4]/i').click()
            driver.find_element_by_xpath(r'//*[@id="ant"]/div[6]/div/div/div/button').click()
            break
        except Exception as k:
            print(k)
    while(True):
        temp = 'https://dropmail.me/api/graphql/web-test-IDacHoa?query=query%20(%24id%3A%20ID!)%20%7Bsession(id%3A%24id)%20%7B%20addresses%20%7Baddress%7D%2C%20mails%7BrawSize%2C%20fromAddr%2C%20toAddr%2C%20downloadUrl%2C%20text%2C%20headerSubject%7D%7D%20%7D&variables=%7B%22id%22%3A%22fuck%22%7D'.replace('fuck',id)
        noidung = requests.get(temp).text
        if 'Melo' in noidung:
            result = re.findall(r'(?<=into your browser: ).*?(?=\\n)',noidung)
            break
    print(result)
    driver.get(result[0])
    driver.get('https://www.melos.studio/login')
    while True:
        try:
            driver.find_element_by_id('nest-messages_email').send_keys(address)
            driver.find_element_by_id('nest-messages_password').send_keys('01653922788Nd')
            driver.find_element_by_xpath(r'//*[@id="ant"]/div[4]/div/div/div/button/span').click()
            break
        except Exception as k:
            print(k)
    while True:
        try:
            
            driver.find_element_by_xpath(r'//*[@id="root"]/div[2]/div/div[1]/div/ul/li[24]/div/div').click()
            driver.find_element_by_xpath(r'//*[@id="Profile$Menu"]/li[2]').click()
            break
        except Exception as k:
            print(k)
    while True:
        try:
            driver.find_element_by_xpath(r'//*[@id="myProfileM"]/div[2]/div[2]/div/div/div[5]/button').click()
            break
        except Exception as k:
            print(k)
    while True:
        try:
            driver.find_element_by_xpath(r'//*[@id="tabWave"]/div/div[2]/div[1]/div[2]/div[1]/div').click()
            break
        except Exception as k:
            print(k)
    while True:
        try:
            
            driver.find_element_by_xpath(r'//*[@id="root"]/div[2]/div/div[1]/div/ul/li[24]/div/div').click()
            driver.find_element_by_xpath(r'//*[@id="Profile$Menu"]/li[5]').click()
            break
        except Exception as k:
            print(k)

driver.quit()
