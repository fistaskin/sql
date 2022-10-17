from selenium import webdriver
from selenium.webdriver.support.ui import Select
import os

hosts = list(open('targets.txt'))
d = webdriver.Chrome()
os.system('timeout 2')

d.get('http://127.0.0.1:8080')
login = d.find_element_by_id('loginUser')
password = d.find_element_by_id('loginPass')
submits = d.find_elements_by_tag_name('span')

login.send_keys('admin')
password.send_keys('admin')
submits[52].click()

os.system('timeout 2')

new_scan = submits[1]
new_scan.click()

os.system('timeout 2')

submits = d.find_elements_by_tag_name('span')
dropdown = Select(d.find_element_by_id('scanType'))
dropdown.select_by_value('scanList')

urls = d.find_element_by_tag_name('textarea')
urls.send_keys(hosts)
submits[58].click()