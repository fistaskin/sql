# -*- coding: utf-8 -*-

from selenium import webdriver
import os

d = webdriver.Chrome()
os.system('timeout 10')
page = 370
while(1):
 try:
  hosts = open('C://OSPanel//domains//new//results//'+str(page)+'.txt', 'w')
  d.get('https://go.mail.ru/search?fm=1&q=фильмы онлайн&sf='+str(page))
  os.system('timeout 10')

  results = d.find_element_by_class_name('SERP-result')
  links = []
  result = results.find_elements_by_tag_name('li')

  for x in result:
   link = x.find_element_by_tag_name('a').get_attribute('href')
   links.append(link)
  
 
  for x in links:
   hosts.write(x)
   hosts.write('\n')

  hosts.close()

  page = page + 10
 except:
  exit()
