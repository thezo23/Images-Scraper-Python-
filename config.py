from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

global ratio

analysed = 0
duplicate = 0
valid = 0
total = 2000

options = Options()
options.add_argument("user-data-dir=C:\\Users\\Username\\AppData\\Local\\Google\\Chrome\\User Data")  # cookies
options.add_argument('--headless')  # Dont show the browser
