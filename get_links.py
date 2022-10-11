from selenium import webdriver
import os


d = webdriver.Chrome()
os.system('timeout 10')
page = 0
while(1):
 hosts = open('results//'+str(page)+'.txt', 'w')
 d.get('https://go.mail.ru/search?fm=1&q=%D0%BF%D0%BE%D1%80%D0%BD%D0%BE&sf='+str(page))
 os.system('timeout 10')

 results = d.find_elements_by_tag_name('li')

 links = []

 i = 6

 for x in results:
  a = results[i].find_element_by_tag_name('a').get_attribute('href')
  links.append(a)
  i = i + 1
  if i == 18:
   break
 
 for x in links:
  hosts.write(x)
  hosts.write('\n')

 hosts.close()

 page = page + 10
 if page == 620:
  break
